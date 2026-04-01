from gtts import gTTS
import os
import time

def generate_speech(text, emotion, intensity):
    # unique filename using timestamp
    filename = f"static/output_{int(time.time())}.mp3"

    slow = False

    if emotion in ["sadness", "fear"]:
        slow = True

    elif emotion in ["joy"]:
        slow = False

    # intensity effect
    if intensity > 0.8:
        text = text.upper() + "!!!"

    tts = gTTS(text=text, lang='en', slow=slow)
    tts.save(filename)

    return filename