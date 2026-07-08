import streamlit as st
from streamlit_mic_recorder import mic_recorder
import assemblyai as aai
from deep_translator import GoogleTranslator

# Enter your AssemblyAI API Key
aai.settings.api_key = "ef3b0c7ecbb1433a996f05adf2e3ad11"

st.set_page_config(
    page_title="Multilingual Speech Recognition",
    page_icon="🎤",
    layout="centered"
)

st.title("🎤 Multilingual Speech Recognition and Translation")

st.write(
    "Speak in your preferred language and translate it into English."
)

language_dict = {
    "English": "en",
    "Kannada": "kn",
    "Hindi": "hi",
    "Tamil": "ta",
    "Malayalam": "ml"
}

selected_language = st.selectbox(
    "Select your Language",
    list(language_dict.keys())
)

audio = mic_recorder(
    start_prompt="🎙️ Start Recording",
    stop_prompt="⏹️ Stop Recording",
    key="mic"
)

if audio:

    st.success("🎉 Audio captured successfully!")

    transcriber = aai.Transcriber()

    config = aai.TranscriptionConfig(
        language_code=language_dict[selected_language]
    )

    transcript = transcriber.transcribe(
        audio["bytes"],
        config=config
    )

    if transcript.status == "error":
        st.error(transcript.error)

    else:
        text = transcript.text

        st.subheader("Recognized Text")
        st.success(text)

        translated = GoogleTranslator(
            source=language_dict[selected_language],
            target="en"
        ).translate(text)

        st.subheader("English Translation")
        st.success(translated)