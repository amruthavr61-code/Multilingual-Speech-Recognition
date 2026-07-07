import streamlit as st
import speech_recognition as sr
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Multilingual Speech Recognition")

st.title("🎤 Multilingual Speech Recognition and Translation System")

st.write(
    "An AI-powered application that converts speech from multiple languages into English."
)

recognizer = sr.Recognizer()

if st.button("Start Recording"):
    with sr.Microphone() as source:
        st.write("🎙 Listening... Please speak.")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=5)

            text = recognizer.recognize_google(audio)

            st.success("Speech Recognized Successfully!")

            st.write("Recognized Text:")
            st.write(text)

            translated = GoogleTranslator(
                source="auto",
                target="en"
            ).translate(text)

            st.write("English Translation:")
            st.success(translated)

        except sr.UnknownValueError:
            st.error("Could not understand the speech.")

        except sr.RequestError:
            st.error("Speech Recognition service is unavailable.")

        except Exception as e:
            st.error(f"Error: {e}")