# 🧠 SAFI - Smart Audio Fluency Interface

**SAFI** is a personalized AI system designed to enhance voice recordings by removing stuttering and background noise, then regenerating the speech using your own cloned voice. It combines the power of **Whisper**, **regex-based text cleanup**, and **voice cloning with ElevenLabs** into one seamless pipeline.

---

## 🎯 Features 

- 🔊 **Speech-to-Text**: Uses OpenAI's Whisper to transcribe audio accurately.
- ✂️ **Stutter Removal**: Applies smart regular expressions to clean repeated or stuttered words.
- 🔁 **Voice Cloning**: Clones the user's real voice using ElevenLabs API.
- 🗣️ **Regenerated Output**: Produces a fluent and clear version of the original voice, using the cleaned text and the cloned voice.
- 🔕 **Noise Reduction**: Optional noise suppression via `noisereduce` and `pydub`.

---

## 🛠️ How It Works

1. **Input Audio**: Upload a `.wav` or any other audio file.
2. **Convert & Clean**:
   - Convert audio to mono WAV.
   - Apply noise reduction if needed.
3. **Transcribe**:
   - Transcribe speech using the Whisper model.
4. **Text Cleanup**:
   - Use regex to remove stuttering patterns from text.
5. **Clone Voice**:
   - Clone the speaker's voice from the original audio using ElevenLabs.
6. **Regenerate Audio**:
   - Generate clean, fluent speech using the cleaned text and the cloned voice.

---

## 📦 Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`:
  - `whisper`
  - `noisereduce`
  - `pydub`
  - `ffmpeg-python`
  - `pyttsx3`
  - `requests`
  - `numpy`

> Note: `ffmpeg` must be installed and available in your system PATH.

---


