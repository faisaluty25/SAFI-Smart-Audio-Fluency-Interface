# import streamlit as st
# import os
# import uuid
# import tempfile
# from processor import AudioProcessing

# # === Configuration ===
# ELEVENLABS_API_KEY = "sk_7d8382f3856f876ea9d441b2330c341cb561e3f221eb663e"
# BASE_DIR = "stutter_sessions"
# os.makedirs(BASE_DIR, exist_ok=True)

# # Initialize processor
# audio_processor = AudioProcessing(elevenlabs_api_key=ELEVENLABS_API_KEY)

# # === Page config ===
# st.set_page_config(page_title="Welcome to SAFI", layout="centered")
# st.title("🎤 Welcome to SAFI")
# st.markdown("An intelligent audio processing platform")

# # === Upload UI ===
# uploaded_file = st.file_uploader("Drag and drop file here", type=["wav", "mp3", "m4a", "flac"], label_visibility="collapsed")

# st.markdown("---")

# # === Service Selection Buttons ===
# svc = st.radio("Choose a Service", ["SAFI – Full Audio Cleanup", "Noise Removal", "Text-to-Speech", "Audio Editing"], horizontal=True, index=0)

# # === Processing ===
# if uploaded_file or svc == "Text-to-Speech":

#     if svc == "SAFI – Full Audio Cleanup":
#         st.header("🌀 Full Audio Cleanup")
#         col1, col2 = st.columns(2)

#         with col1:
#             st.markdown("🎧 *Original Audio*")
#             st.audio(uploaded_file)

#         if st.button("✨ Process Audio"):
#             with st.spinner("🔍 Cleaning stutter and cloning voice..."):
#                 try:
#                     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
#                         tmp_file.write(uploaded_file.read())
#                         tmp_path = tmp_file.name

#                     result = audio_processor.process_audio(tmp_path)
#                     os.unlink(tmp_path)

#                     with col2:
#                         st.markdown("🔊 *Cleaned Audio*")
#                         with open(result["clean_audio_path"], "rb") as f:
#                             audio_bytes = f.read()
#                         st.audio(audio_bytes, format="audio/wav")
#                         st.download_button("⬇ Download Cleaned Audio", data=audio_bytes, file_name="cleaned_speech.wav", mime="audio/wav")

#                     with st.expander("📝 View Transcripts"):
#                         st.markdown("*Original Transcription:*")
#                         st.write(result["transcription"].get("text", "No transcription available"))
#                         st.markdown("✅ Cleaned Transcript:")
#                         st.write(result["cleaned_text"])

#                     st.success("✅ Processing complete!")

#                 except Exception as e:
#                     st.error(f"❌ Processing failed: {str(e)}")
#                     if 'tmp_path' in locals() and os.path.exists(tmp_path):
#                         os.unlink(tmp_path)

#     elif svc == "Noise Removal":
#         st.header("🔇 Noise Removal")
#         if st.button("🚫 Remove Noise"):
#             with st.spinner("Filtering noise..."):
#                 session_id = str(uuid.uuid4())
#                 with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
#                     tmp_file.write(uploaded_file.read())
#                     input_path = tmp_file.name

#                 cleaned_path = audio_processor.noise_removal(input_path, session_id)
#                 os.unlink(input_path)

#                 if cleaned_path:
#                     with open(cleaned_path, "rb") as f:
#                         cleaned_audio = f.read()
#                     st.audio(cleaned_audio, format="audio/wav")
#                     st.download_button("⬇ Download Denoised Audio", cleaned_audio, file_name="denoised.wav", mime="audio/wav")
#                     st.success("✅ Noise removed!")
#                 else:
#                     st.error("❌ Noise removal failed")

#     elif svc == "Text-to-Speech":
#         st.header("🗣️ Text-to-Speech")
#         user_text = st.text_area("Enter text:")
#         gender = st.radio("Choose voice", ["Male", "Female"], horizontal=True)
#         voice_ids = {"Male": "yxfudJlxDScRtkww3Dh9", "Female": "pmOnOxdGHHE7D6IIHmqL"}

#         if st.button("🔊 Generate Speech") and user_text:
#             with st.spinner("Synthesizing voice..."):
#                 session_id = str(uuid.uuid4())
#                 output_path = os.path.join("audio_processing", session_id, f"tts_{session_id}.wav")
#                 os.makedirs(os.path.dirname(output_path), exist_ok=True)
#                 voice_id = voice_ids[gender]
#                 audio_path = audio_processor.generate_audio(user_text, voice_id, output_path)

#                 with open(audio_path, "rb") as f:
#                     audio_bytes = f.read()
#                 st.audio(audio_bytes, format="audio/wav")
#                 st.download_button("⬇ Download TTS Audio", audio_bytes, file_name="speech.wav", mime="audio/wav")

#     elif svc == "Audio Editing":
#         st.warning("🔧 Audio Editing feature coming soon. Please use another service for now.")


# import streamlit as st
# import os
# import uuid
# import tempfile
# import requests
# from processor import AudioProcessing

# # === Configuration ===
# ELEVENLABS_API_KEY = "sk_7d8382f3856f876ea9d441b2330c341cb561e3f221eb663e"
# BASE_DIR = "stutter_sessions"
# os.makedirs(BASE_DIR, exist_ok=True)

# # Initialize processor
# audio_processor = AudioProcessing(elevenlabs_api_key=ELEVENLABS_API_KEY)

# # === Page config ===
# st.set_page_config(page_title="Welcome to SAFI", layout="centered")
# st.title("🎤 Welcome to SAFI")
# st.markdown("An intelligent audio processing platform")

# # === Upload UI ===
# uploaded_file = st.file_uploader("Drag and drop file here", type=["wav", "mp3", "m4a", "flac"], label_visibility="collapsed")

# st.markdown("---")

# # === Service Selection Buttons ===
# svc = st.radio("Choose a Service", ["SAFI – Full Audio Cleanup", "Noise Removal", "Text-to-Speech", "Audio Editing"], horizontal=True, index=0)

# # === Processing ===
# if uploaded_file or svc == "Text-to-Speech":

#     if svc == "SAFI – Full Audio Cleanup":
#         st.header("🌀 Full Audio Cleanup")
#         col1, col2 = st.columns(2)

#         with col1:
#             st.markdown("🎧 *Original Audio*")
#             st.audio(uploaded_file)

#         if st.button("✨ Process Audio"):
#             with st.spinner("🔍 Cleaning stutter and cloning voice..."):
#                 try:
#                     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
#                         tmp_file.write(uploaded_file.read())
#                         tmp_path = tmp_file.name

#                     result = audio_processor.process_audio(tmp_path)
#                     os.unlink(tmp_path)

#                     with col2:
#                         st.markdown("🔊 *Cleaned Audio*")
#                         with open(result["clean_audio_path"], "rb") as f:
#                             audio_bytes = f.read()
#                         st.audio(audio_bytes, format="audio/wav")
#                         st.download_button("⬇ Download Cleaned Audio", data=audio_bytes, file_name="cleaned_speech.wav", mime="audio/wav")

#                     with st.expander("📝 View Transcripts"):
#                         st.markdown("*Original Transcription:*")
#                         st.write(result["transcription"].get("text", "No transcription available"))
#                         st.markdown("✅ Cleaned Transcript:")
#                         st.write(result["cleaned_text"])

#                     st.success("✅ Processing complete!")

#                 except Exception as e:
#                     st.error(f"❌ Processing failed: {str(e)}")
#                     if 'tmp_path' in locals() and os.path.exists(tmp_path):
#                         os.unlink(tmp_path)

#     elif svc == "Noise Removal":
#         st.header("🔇 Noise Removal")
#         if st.button("🚫 Remove Noise"):
#             with st.spinner("Filtering noise..."):
#                 session_id = str(uuid.uuid4())
#                 with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
#                     tmp_file.write(uploaded_file.read())
#                     input_path = tmp_file.name

#                 cleaned_path = audio_processor.noise_removal(input_path, session_id)
#                 os.unlink(input_path)

#                 if cleaned_path:
#                     with open(cleaned_path, "rb") as f:
#                         cleaned_audio = f.read()
#                     st.audio(cleaned_audio, format="audio/wav")
#                     st.download_button("⬇ Download Denoised Audio", cleaned_audio, file_name="denoised.wav", mime="audio/wav")
#                     st.success("✅ Noise removed!")
#                 else:
#                     st.error("❌ Noise removal failed")

#     elif svc == "Text-to-Speech":
#         st.header("🗣️ Text-to-Speech")
#         user_text = st.text_area("Enter text:")

#         # Fetch voice IDs from ElevenLabs
#         @st.cache_data
#         def fetch_voices():
#             url = "https://api.elevenlabs.io/v1/voices"
#             headers = {"xi-api-key": ELEVENLABS_API_KEY}
#             response = requests.get(url, headers=headers)
#             if response.status_code == 200:
#                 return response.json().get("voices", [])
#             return []

#         voices = fetch_voices()
#         voice_names = [f"{v['name']} ({v['voice_id'][:6]})" for v in voices]
#         selected_voice = st.selectbox("Choose a Voice", voice_names)
#         selected_voice_id = next((v['voice_id'] for v in voices if selected_voice.startswith(v['name'])), None)

#         if st.button("🔊 Generate Speech") and user_text and selected_voice_id:
#             with st.spinner("Synthesizing voice..."):
#                 session_id = str(uuid.uuid4())
#                 output_path = os.path.join("audio_processing", session_id, f"tts_{session_id}.wav")
#                 os.makedirs(os.path.dirname(output_path), exist_ok=True)
#                 audio_path = audio_processor.generate_audio(user_text, selected_voice_id, output_path)

#                 with open(audio_path, "rb") as f:
#                     audio_bytes = f.read()
#                 st.audio(audio_bytes, format="audio/wav")
#                 st.download_button("⬇ Download TTS Audio", audio_bytes, file_name="speech.wav", mime="audio/wav")

#     elif svc == "Audio Editing":
#         st.warning("🔧 Audio Editing feature coming soon. Please use another service for now.")


import streamlit as st
import os
import uuid
import tempfile
import requests
import io
from pydub import AudioSegment
from processor import AudioProcessing

# === Configuration ===
ELEVENLABS_API_KEY = "sk_7d8382f3856f876ea9d441b2330c341cb561e3f221eb663e"
BASE_DIR = "stutter_sessions"
os.makedirs(BASE_DIR, exist_ok=True)

# Initialize processor
audio_processor = AudioProcessing(elevenlabs_api_key=ELEVENLABS_API_KEY)

# === Page config ===
st.set_page_config(page_title="Welcome to SAFI", layout="centered")
st.title("🎤 Welcome to SAFI")
st.markdown("An intelligent audio processing platform")

# === Upload UI ===
uploaded_file = st.file_uploader("Drag and drop file here", type=["wav", "mp3", "m4a", "flac"], label_visibility="collapsed")

st.markdown("---")

# === Service Selection Buttons ===
svc = st.radio("Choose a Service", ["SAFI – Full Audio Cleanup", "Noise Removal", "Text-to-Speech", "Audio Editing"], horizontal=True, index=0)

# === Processing ===
if uploaded_file or svc == "Text-to-Speech":

    if svc == "SAFI – Full Audio Cleanup":
        st.header("🌀 Full Audio Cleanup")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("🎧 *Original Audio*")
            st.audio(uploaded_file)

        if st.button("✨ Process Audio"):
            with st.spinner("🔍 Cleaning stutter and cloning voice..."):
                try:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                        tmp_file.write(uploaded_file.read())
                        tmp_path = tmp_file.name

                    result = audio_processor.process_audio(tmp_path)
                    os.unlink(tmp_path)

                    with col2:
                        st.markdown("🔊 *Cleaned Audio*")
                        with open(result["clean_audio_path"], "rb") as f:
                            audio_bytes = f.read()
                        st.audio(audio_bytes, format="audio/wav")
                        st.download_button("⬇ Download Cleaned Audio", data=audio_bytes, file_name="cleaned_speech.wav", mime="audio/wav")

                    with st.expander("📝 View Transcripts"):
                        st.markdown("*Original Transcription:*")
                        st.write(result["transcription"].get("text", "No transcription available"))
                        st.markdown("✅ Cleaned Transcript:")
                        st.write(result["cleaned_text"])

                    st.success("✅ Processing complete!")

                except Exception as e:
                    st.error(f"❌ Processing failed: {str(e)}")
                    if 'tmp_path' in locals() and os.path.exists(tmp_path):
                        os.unlink(tmp_path)

    elif svc == "Noise Removal":
        st.header("🔇 Noise Removal")
        if st.button("🚫 Remove Noise"):
            with st.spinner("Filtering noise..."):
                session_id = str(uuid.uuid4())
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                    tmp_file.write(uploaded_file.read())
                    input_path = tmp_file.name

                cleaned_path = audio_processor.noise_removal(input_path, session_id)
                os.unlink(input_path)

                if cleaned_path:
                    with open(cleaned_path, "rb") as f:
                        cleaned_audio = f.read()
                    st.audio(cleaned_audio, format="audio/wav")
                    st.download_button("⬇ Download Denoised Audio", cleaned_audio, file_name="denoised.wav", mime="audio/wav")
                    st.success("✅ Noise removed!")
                else:
                    st.error("❌ Noise removal failed")

    elif svc == "Text-to-Speech":
        st.header("🗣️ Text-to-Speech")
        user_text = st.text_area("Enter text:")

        @st.cache_data
        def fetch_voices():
            url = "https://api.elevenlabs.io/v1/voices"
            headers = {"xi-api-key": ELEVENLABS_API_KEY}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json().get("voices", [])
            return []

        voices = fetch_voices()
        voice_names = [f"{v['name']} ({v['voice_id'][:6]})" for v in voices]
        selected_voice = st.selectbox("Choose a Voice", voice_names)
        selected_voice_id = next((v['voice_id'] for v in voices if selected_voice.startswith(v['name'])), None)

        if st.button("🔊 Generate Speech") and user_text and selected_voice_id:
            with st.spinner("Synthesizing voice..."):
                session_id = str(uuid.uuid4())
                output_path = os.path.join("audio_processing", session_id, f"tts_{session_id}.wav")
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                audio_path = audio_processor.generate_audio(user_text, selected_voice_id, output_path)

                with open(audio_path, "rb") as f:
                    audio_bytes = f.read()
                st.audio(audio_bytes, format="audio/wav")
                st.download_button("⬇ Download TTS Audio", audio_bytes, file_name="speech.wav", mime="audio/wav")

    elif svc == "Audio Editing":
        st.header("🎛️ Audio Editing")
        try:
            session_id = str(uuid.uuid4())
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_path = tmp_file.name

            wav_path = audio_processor.convert_to_wav(tmp_path, session_id)
            transcription = audio_processor.transcribe_audio(wav_path)
            words = transcription['text'].split()
            audio = AudioSegment.from_wav(wav_path)
            duration_per_word = len(audio) / max(1, len(words))
            keep_words = [True] * len(words)

            st.info("Uncheck any words you'd like removed and click Apply Edits.")
            for i, word in enumerate(words):
                cols = st.columns([1, 4, 2])
                with cols[0]:
                    keep_words[i] = st.checkbox("", value=True, key=f"word_{i}")
                with cols[1]:
                    st.markdown(f"**{word}**")
                with cols[2]:
                    start = int(i * duration_per_word)
                    end = int((i + 1) * duration_per_word)
                    segment = audio[start:end]
                    buf = io.BytesIO()
                    segment.export(buf, format="wav")
                    st.audio(buf.getvalue(), format="audio/wav")

            if st.button("Apply Edits"):
                edited_audio = AudioSegment.empty()
                for i, keep in enumerate(keep_words):
                    if keep:
                        start = int(i * duration_per_word)
                        end = int((i + 1) * duration_per_word)
                        edited_audio += audio[start:end]

                edited_path = os.path.join(audio_processor._create_session_dir(session_id), f"edited_{session_id}.wav")
                edited_audio.export(edited_path, format="wav")
                st.success("✅ Editing complete!")

                with open(edited_path, "rb") as f:
                    audio_bytes = f.read()
                st.audio(audio_bytes, format="audio/wav")
                st.download_button("⬇ Download Edited Audio", audio_bytes, file_name="edited_audio.wav", mime="audio/wav")

        except Exception as e:
            st.error(f"❌ Audio Editing failed: {str(e)}")
