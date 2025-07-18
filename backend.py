import os
import uuid
import noisereduce as nr
import numpy as np
from pydub import AudioSegment
import ffmpeg

import whisper
import pyttsx3
import re
import shutil
import requests
import json
from whisper.audio import load_audio  # <-- Import Whisper's load_audio here

class AudioProcessing:
    def _init_(self, elevenlabs_api_key=None):
        self.ELEVENLABS_API_KEY = elevenlabs_api_key or "YOUR_ELEVENLABS_API_KEY"
        self.BASE_DIR = "audio_processing"
        self.whisper_model = whisper.load_model("base")
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)
        self.tts_engine.setProperty('volume', 0.9)
        os.makedirs(self.BASE_DIR, exist_ok=True)

    def _create_session_dir(self, session_id):
        session_dir = os.path.join(self.BASE_DIR, session_id)
        os.makedirs(session_dir, exist_ok=True)
        return session_dir

    def _save_input_file(self, uploaded_file, session_id):
        session_dir = self._create_session_dir(session_id)
        input_path = os.path.join(session_dir, f"uploaded_{session_id}.wav")
        with open(input_path, "wb") as f:
            f.write(uploaded_file.read())
        return input_path

    def convert_to_wav(self, input_path: str, session_id: str):
        try:
            session_dir = self._create_session_dir(session_id)
            output_file = os.path.join(session_dir, f"converted_{session_id}.wav")
            (
                ffmpeg
                .input(input_path)
                .output(output_file, acodec='pcm_s16le', ar=44100, ac=1)
                .run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
            )
            return output_file
        except ffmpeg.Error as e:
            print(f"FFmpeg error:\n{e.stderr.decode()}")
            return None

    def noise_removal(self, input_path: str, session_id: str):
        wav_path = self.convert_to_wav(input_path, session_id)
        if not wav_path:
            return None

        try:
            audio = AudioSegment.from_wav(wav_path)
            if audio.channels > 1:
                audio = audio.set_channels(1)
            samples = np.array(audio.get_array_of_samples()).astype(np.float32)
            samples /= np.max(np.abs(samples), initial=1)
            reduced_noise = nr.reduce_noise(y=samples, sr=audio.frame_rate)
            reduced_noise = (reduced_noise * 32767).astype(np.int16)
            cleaned_audio = AudioSegment(
                reduced_noise.tobytes(),
                frame_rate=audio.frame_rate,
                sample_width=2,
                channels=1
            )
            output_path = os.path.join(self._create_session_dir(session_id), f"denoised{session_id}.wav")
            cleaned_audio.export(output_path, format="wav")
            return output_path
        except Exception as e:
            print(f"Noise removal error: {str(e)}")
            return None

    def text_to_audio(self, text: str, session_id: str):
        try:
            output_path = os.path.join(self._create_session_dir(session_id), f"tts{session_id}.wav")
            self.tts_engine.save_to_file(text, output_path)
            self.tts_engine.runAndWait()
            return output_path
        except Exception as e:
            print(f"TTS error: {str(e)}")
            return None

    def transcribe_audio(self, audio_path: str) -> dict:
        audio_waveform = load_audio(audio_path)
        return self.whisper_model.transcribe(audio_waveform, language="en")

    def remove_stutter(self, text: str) -> str:
        text = re.sub(r'\b(\w)(-\1){1,}\b', r'\1', text)
        text = re.sub(r'(\w)\1{2,}', r'\1', text)
        text = re.sub(r'\b(\w{1,3})([.,]?\s+\1){1,}\b', r'\1', text)
        text = re.sub(r'\b(\w+)([.,]?\s+\1){1,}\b', r'\1', text)
        text = re.sub(r'\b(\w+)([.,]?)\s+\1\b([.,]?)', r'\1\2', text, flags=re.IGNORECASE)
        return text

    def clone_voice(self, audio_path, clone_name="user_voice"):
        url = "https://api.elevenlabs.io/v1/voices/add"
        headers = {
            "xi-api-key": self.ELEVENLABS_API_KEY,
        }
        files = {
            "name": (None, clone_name),
            "files": (audio_path, open(audio_path, "rb"), "audio/wav")
        }
        response = requests.post(url, headers=headers, files=files)
        if response.status_code == 200:
            return response.json()["voice_id"]
        else:
            raise Exception(f"Voice clone failed: {response.text}")

    def generate_audio(self, text, voice_id, output_path):
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {
            "xi-api-key": self.ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "text": text,
            "voice_settings": {
                "stability": 0.75,
                "similarity_boost": 0.75
            }
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(response.content)
            return output_path
        else:
            raise Exception(f"Audio generation failed: {response.text}")

    def process_audio(self, input_audio):
        session_id = str(uuid.uuid4())
        try:
            if hasattr(input_audio, 'read'):
                original_path = self._save_input_file(input_audio, session_id)
            elif isinstance(input_audio, str) and os.path.exists(input_audio):
                session_dir = self._create_session_dir(session_id)
                original_path = os.path.join(session_dir, f"copied_{session_id}.wav")
                shutil.copy(input_audio, original_path)
            else:
                raise Exception("Unsupported input type for audio")

            wav_path = self.convert_to_wav(original_path, session_id)
            if wav_path is None:
                raise Exception("Audio conversion failed")

            transcription = self.transcribe_audio(wav_path)
            cleaned_text = self.remove_stutter(transcription['text'])
            voice_id = self.clone_voice(wav_path)
            clean_audio_path = self.generate_audio(cleaned_text, voice_id,
                os.path.join(self._create_session_dir(session_id), f"cleaned{session_id}.wav"))

            return {
                "session_id": session_id,
                "original_path": original_path,
                "wav_path": wav_path,
                "transcription": transcription,
                "cleaned_text": cleaned_text,
                "clean_audio_path": clean_audio_path
            }
        except Exception as e:
            self.cleanup_session(session_id)
            raise Exception(f"Processing failed: {str(e)}")

    def cleanup_session(self, session_id: str):
        session_dir = os.path.join(self.BASE_DIR, session_id)
        if os.path.exists(session_dir):
            shutil.rmtree(session_dir)