import streamlit as st
import os
from transformers import pipeline
import whisper

st.title("AI Interview Analyzer")

# Load HF emotion pipeline (global for efficiency)
@st.cache_resource
def load_emotion_model():
    return pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base"
    )

emotion_pipeline = load_emotion_model()

# Text input analysis
text_input = st.text_area("Enter your interview response (or transcribed text):")
if st.button("Analyze Text") and text_input:
    result = emotion_pipeline(text_input)
    
    # Filler word detection
    filler_words = ["um", "uh", "like", "you know"]
    filler_count = sum(text_input.lower().count(word) for word in filler_words)
    
    st.subheader("Analysis Results")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Emotion", result[0]['label'])
    with col2:
        st.metric("Confidence", f"{result[0]['score']:.2%}")
    with col3:
        st.metric("Filler Words", filler_count)
    
    # Feedback
    if filler_count > 3:
        st.warning("⚠️ Too many filler words. Practice pausing instead.")
    else:
        st.success("✅ Good clarity.")
    
    if result[0]['label'] in ["nervous", "fear"]:
        st.warning("💡 Try speaking more confidently.")
    else:
        st.success("✅ Confident delivery.")

# Audio upload and transcription
audio_file = st.file_uploader("Upload audio (WAV/MP3)", type=["wav", "mp3"])

if audio_file:
    # Save temp file
    temp_path = "temp_audio.wav"
    with open(temp_path, "wb") as f:
        f.write(audio_file.read())
    
    try:
        with st.spinner("Transcribing..."):
            # Load Whisper on demand
            whisper_model = whisper.load_model("base")
            result_audio = whisper_model.transcribe(temp_path)
            transcribed_text = result_audio["text"]
        
        st.subheader("Transcribed Text")
        st.text_area("", transcribed_text, height=100, key="transcribed")
        
        # Auto-analyze transcribed text
        if st.button("Analyze Transcription"):
            text_input = transcribed_text  # Trigger analysis above
            
    except Exception as e:
        st.error(f"Transcription error: {str(e)}")
    
    finally:
        # Always cleanup
        if os.path.exists(temp_path):
            os.remove(temp_path)
