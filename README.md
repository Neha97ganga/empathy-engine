# 🎙️ Empathy Engine

## 🚀 Overview

The Empathy Engine is an AI-powered system that converts text into emotionally expressive speech. Unlike traditional Text-to-Speech systems that produce monotonic audio, this application detects the underlying emotion of the input text and dynamically modifies speech output to create a more human-like interaction.

---

## ✨ Features

* 🧠 Emotion detection using a Transformer-based model (Hugging Face)
* 🎭 Supports multiple emotions: joy, sadness, anger, fear, surprise
* 📊 Intensity scaling based on emotion confidence
* 🔊 Natural speech generation using Google Text-to-Speech (gTTS)
* 🌐 Interactive web interface using Flask
* ⚡ Real-time audio playback
* 🔄 Cache-busting for smooth performance

---

## 🏗️ Project Structure

```
empathy-engine/
│
├── app.py
├── emotion.py
├── tts.py
├── static/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/Neha97ganga/empathy-engine.git
cd empathy-engine
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run the Application

```
python app.py
```

### 4. Open in Browser

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

### 1. Emotion Detection

The system uses a pre-trained Hugging Face transformer model:

`j-hartmann/emotion-english-distilroberta-base`

This model classifies input text into emotions such as:

* Joy
* Sadness
* Anger
* Fear
* Surprise

It also provides a confidence score used as emotion intensity.

---

### 2. Emotion → Voice Mapping

| Emotion | Voice Behavior               |
| ------- | ---------------------------- |
| Joy     | Faster, energetic speech     |
| Sadness | Slower, softer speech        |
| Anger   | Emphasized (uppercase + !!!) |
| Fear    | Slow, cautious tone          |
| Neutral | Balanced tone                |

---

### 3. Intensity Scaling

The confidence score from the model determines how expressive the speech becomes:

* High intensity → Uppercase text + exclamation marks
* Low intensity → Normal speech

---

### 4. Speech Generation

We use **gTTS (Google Text-to-Speech)**:

* Produces natural-sounding audio
* Supports dynamic speed variation
* Outputs `.mp3` audio files

---

### 5. UI & Performance Improvements

* Flask-based web interface
* Real-time response
* Unique filenames for audio generation
* Cache-busting to avoid delays

---

## 🎯 Design Decisions

* Used Transformers instead of basic sentiment tools for better accuracy
* Used gTTS instead of pyttsx3 for natural voice output
* Modular design with separate files for emotion detection and TTS
* Implemented caching fixes for smooth user experience

---
