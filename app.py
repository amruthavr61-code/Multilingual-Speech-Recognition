import streamlit as st
from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr
from deep_translator import GoogleTranslator
import tempfile

st.set_page_config(page_title="Multilingual Speech Recognition", page_icon="🎤")

st.title("🎤 Multilingual Speech Recognition and Translation System")

st.write(
    "Speak in your selected language and translate it into English."
)

language_dict = {
    "English": "en-IN",
    "Kannada": "kn-IN",
    "Hindi": "hi-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Malayalam": "ml-IN"
}

selected_language = st.selectbox(
    "Select the language you will speak",
    list(language_dict.keys())
)

audio = mic_recorder(
    start_prompt="🎙️ Start Recording",
    stop_prompt="⏹️ Stop Recording",
    key="recorder",
)

if audio:
    st.success("Recording completed!")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio["bytes"])
        audio_path = f.name

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(
            audio_data,
            language=language_dict[selected_language]
        )

        st.subheader("Recognized Text")
        st.success(text)

        translated = GoogleTranslator(
            source="auto",
            target="en"
        ).translate(text)

        st.subheader("English Translation")
        st.success(translated)

    except sr.UnknownValueError:
        st.error("Could not understand your speech.")

    except sr.RequestError:
        st.error("Speech Recognition service is unavailable.")

    except Exception as e:
        st.error(f"Error: {e}")