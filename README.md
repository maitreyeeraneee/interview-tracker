# 🚀 Interview Analyzer

**AI-Powered Interview Practice Tool**  
A Streamlit web app that analyzes interview responses via text or audio input. Detects emotions, identifies filler words, and provides actionable feedback to help users improve clarity and confidence. Built with Hugging Face ML models for production-ready performance.

## 📋 Features
- 🎤 **Audio Upload & Transcription**: Upload WAV/MP3 files; Whisper automatically transcribes speech to text.
- 📝 **Text Input Analysis**: Direct text entry for quick practice sessions.
- 😊 **Emotion Classification**: Real-time detection of emotions (e.g., confident, nervous) with confidence scores.
- 🗣️ **Filler Word Detection**: Counts & flags fillers like 'um', 'uh', 'like', 'you know'.
- 💬 **Smart Feedback**: Personalized tips, e.g., 'Too many fillers - improve clarity' or 'Sound more confident'.
- ⚡ **Instant Results**: Web-based UI with success/warning badges for intuitive UX.

## 🛠️ Tech Stack
- **Frontend/Backend**: [Streamlit](https://streamlit.io/) (Python web framework)
- **ML Models**: 
  - Hugging Face Transformers
  - Emotion: [j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base)
  - Transcription: [Whisper (base)](https://openai.com/research/whisper)
- **Deep Learning**: PyTorch
- **Deployment**: `streamlit run app.py`

## 🤖 Hugging Face Implementation
Leverages HF `pipeline` API for zero-shot integration:
```python
emotion = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
result = emotion(text)
```
- Processes transcribed text for emotion labels/scores.
- Whisper loaded via `whisper.load_model("base")` for audio-to-text.
- Seamless: No custom training; pre-trained models for accuracy & speed.

## 📁 Project Structure
```
ai-interview-analyzer/
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies
├── README.md           # This file
├── .gitignore          # Git ignores
└── TODO.md            # Progress tracking
```

## 💡 What I Learned
- Integrating HF pipelines & Whisper for end-to-end ML in web apps.
- Building interactive UIs with Streamlit for rapid prototyping.
- Audio processing pipelines (upload → transcribe → analyze).
- Creating user-centric feedback systems with conditional logic.
- Best practices for ML deployment: model loading, temp file handling, UI polish.

---

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
Ready for interviews! 🎯 Run `pip install -r requirements.txt && streamlit run app.py`.

