# Interview Analyzer🎙️

**Streamlit web app for analyzing interview responses via text or audio. Detects emotions, filler words, and provides feedback using Hugging Face models.**

## Overview ✨

AI Interview Analyzer helps candidates improve their interview performance by analyzing both **text and audio responses**. It leverages state-of-the-art NLP models to detect emotions, identify filler words, and generate personalized feedback.

Built with a focus on **real-world usability**, this project demonstrates applied machine learning, audio processing, and UI deployment.

---

## Key Features

🎤 **Multi-Input Support**
- Text input for quick analysis  
- Audio upload (WAV/MP3) with automatic transcription  
🗣️ **Speech-to-Text**
- Converts audio responses into text using Whisper  
😊 **Emotion Detection**
- Detects emotional tone (e.g., confident, nervous, neutral)  
- Provides confidence scores for each prediction  
🔍 **Filler Word Analysis**
- Identifies overused filler words:
  - *um, uh, like, you know, basically*  
💡 **Smart Feedback Engine**
- Provides structured suggestions on:
  - Clarity  
  - Confidence  
  - Communication style  

---

## Tech Stack 🛠️
| Component | Technology |
|-----------|------------|
| Framework | [Streamlit](https://streamlit.io/) |
| Emotion Model | [j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) (Transformers pipeline) |
| Transcription | [Whisper base](https://openai.com/research/whisper) |
| Backend | PyTorch |

## Hugging Face Implementation 🤗
Zero-shot integration using `pipeline` API for efficiency:

```python
from transformers import pipeline
emotion = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
result = emotion(text)  # Returns [{'label': 'joy', 'score': 0.95}]
```

- Processes transcribed text directly.
- No custom training; leverages pre-trained models for speed and accuracy.
- Whisper loaded via `whisper.load_model("base")`.


##  Whisper Integration 🎵
 
```python
import whisper

model = whisper.load_model("base")
result = model.transcribe(audio_file)
text = result["text"]

-Converts spoken responses → structured text
-Handles different accents reasonably well
-Enables seamless pipeline: Audio → Text → Emotion Analysis
```
---

## Quick Start🚀

```
pip install -r requirements.txt
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.


## Project Files📦 

Interview-Analyzer

-app.py              # Main Streamlit application
-requirements.txt    # Project dependencies
-README.md           # Project documentation

---

## What I Learned 📚
-Practical implementation of NLP pipelines using Hugging Face Transformers
-Integration of speech-to-text systems (Whisper)
-Building and deploying interactive ML apps with Streamlit
-Designing end-to-end ML workflows
-Writing clean, production-level Python code

---

## 🤝 Let's Connect!
If you found this project interesting or want to collaborate, feel free to reach out. Contributions, feedback, and ideas are always welcome — let's build something great!! 🚀

---
