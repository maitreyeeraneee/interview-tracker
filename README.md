# AI Interview Analyzer

**Streamlit web app for analyzing interview responses via text or audio. Detects emotions, filler words, and provides feedback using Hugging Face models.**

## Features
- Text input or audio upload (WAV/MP3) with automatic transcription via Whisper.
- Emotion classification (e.g., confident, nervous) with confidence scores.
- Filler word detection (um, uh, like, you know).
- Personalized feedback on clarity and tone.

## Tech Stack
| Component | Technology |
|-----------|------------|
| Framework | [Streamlit](https://streamlit.io/) |
| Emotion Model | [j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) (Transformers pipeline) |
| Transcription | [Whisper base](https://openai.com/research/whisper) |
| Backend | PyTorch |

## Hugging Face Implementation
Zero-shot integration using `pipeline` API for efficiency:

```python
from transformers import pipeline
emotion = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
result = emotion(text)  # Returns [{'label': 'joy', 'score': 0.95}]
```

- Processes transcribed text directly.
- No custom training; leverages pre-trained models for speed and accuracy.
- Whisper loaded via `whisper.load_model("base")`.

## Quick Start
```bash
pip install -r requirements.txt
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

## Project Files
- `app.py`: Main application logic.
- `requirements.txt`: Dependencies.

