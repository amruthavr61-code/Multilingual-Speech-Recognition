import streamlit as st
import speech_recognition as sr
from googletrans import Translator

st.set_page_config(page_title="Multilingual Speech Recognition")

st.title("🎤 Multilingual Speech Recognition and Translation System")

st.write("An AI-powered application that converts speech from multiple languages into text and translates it into English.")

recognizer = sr.Recognizer()
translator = Translator()

if st.button("Start Recording"):
    with sr.Microphone() as source:
        st.write("🎙️ Listening... Please speak.")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=5)

            text = recognizer.recognize_google(audio)

            st.success("Speech Recognized Successfully!")
            st.write("Recognized Text:")
            st.write(text)

            translated = translator.translate(text, dest="en")

            st.write("English Translation:")
            st.success(translated.text)

        except sr.UnknownValueError:
            st.error("Could not understand the speech.")

        except sr.RequestError:
            st.error("Network/API error.")

        except Exception as e:
            st.error(f"Error: {e}")