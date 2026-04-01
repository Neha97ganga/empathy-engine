import pyttsx3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# ---------------------------
# INIT
# ---------------------------
engine = pyttsx3.init()
analyzer = SentimentIntensityAnalyzer()

# ---------------------------
# EMOTION DETECTION
# ---------------------------
def detect_emotion(text):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.5:
        return "happy"
    elif compound <= -0.5:
        return "frustrated"
    else:
        return "neutral"

# ---------------------------
# VOICE MAPPING
# ---------------------------
def apply_voice_settings(emotion):
    if emotion == "happy":
        engine.setProperty('rate', 220)   # faster
        engine.setProperty('volume', 1.0)

    elif emotion == "frustrated":
        engine.setProperty('rate', 120)   # slower
        engine.setProperty('volume', 0.6)

    else:
        engine.setProperty('rate', 160)
        engine.setProperty('volume', 0.9)

# ---------------------------
# GENERATE AUDIO
# ---------------------------
def generate_audio(text, filename="output.wav"):
    emotion = detect_emotion(text)
    print(f"Detected Emotion: {emotion}")

    apply_voice_settings(emotion)

    engine.save_to_file(text, filename)
    engine.runAndWait()

    print(f"Audio saved as {filename}")

# ---------------------------
# MAIN
# ---------------------------
if __name__ == "__main__":
    user_text = input("Enter your text: ")
    generate_audio(user_text)