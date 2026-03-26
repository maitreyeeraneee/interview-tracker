import streamlit as st
from transformers import pipeline

# Load HF model
emotion = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)

st.title("🎤 AI Interview Analyzer")

# Text input
text = st.text_area("Enter your interview answer:")

if st.button("Analyze"):
    if text:
        result = emotion(text)

        # Filler words
        filler_words = ["um", "uh", "like", "you know"]
        count = sum(text.lower().count(word) for word in filler_words)

        st.subheader("Results:")
        st.write("Emotion:", result[0]['label'])
        st.write("Confidence Score:", result[0]['score'])
        st.write("Filler Words:", count)

        # Feedback
        if count > 3:
            st.warning("Too many filler words")
        else:
            st.success("Good clarity")

        if result[0]['label'] in ["nervous", "fear"]:
            st.warning("Try to sound more confident")
        else:
            st.success("Confident tone")

import whisper

model = whisper.load_model("base")

audio_file = st.file_uploader("Upload audio", type=["wav", "mp3"])

if audio_file:
    with open("temp.wav", "wb") as f:
        f.write(audio_file.read())

    result_audio = model.transcribe("temp.wav")
    text = result_audio["text"]
    st.write("Transcribed Text:", text)