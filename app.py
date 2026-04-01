from flask import Flask, request, jsonify
from emotion import detect_emotion
from tts import generate_speech

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Empathy Engine</title>
<style>
body {
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    text-align: center;
    padding: 40px;
}

.container {
    background: rgba(255,255,255,0.1);
    padding: 30px;
    border-radius: 15px;
    width: 400px;
    margin: auto;
    backdrop-filter: blur(10px);
}

textarea {
    width: 100%;
    padding: 10px;
    border-radius: 10px;
    border: none;
    resize: none;
}

button {
    margin-top: 15px;
    padding: 10px 20px;
    border: none;
    border-radius: 10px;
    background: #ff7a18;
    color: white;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background: #ff9a3c;
}

#result {
    margin-top: 15px;
    font-weight: bold;
}

.loader {
    display: none;
    margin-top: 10px;
}

audio {
    margin-top: 15px;
    width: 100%;
}
</style>
</head>

<body>

<div class="container">
    <h2>🎙️ Empathy Engine</h2>

    <textarea id="text" rows="4" placeholder="Type something emotional..."></textarea>

    <button onclick="sendText()">Generate Voice</button>

    <div class="loader" id="loader">⏳ Generating...</div>

    <p id="result"></p>

    <audio id="audio" controls></audio>
</div>

<script>
function sendText() {
    let text = document.getElementById("text").value;

    if (!text) {
        alert("Enter some text bro 😭");
        return;
    }

    document.getElementById("loader").style.display = "block";
    document.getElementById("result").innerText = "";

    fetch("/process", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text: text})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("loader").style.display = "none";

        let emoji = {
    joy: "😊",
    sadness: "😢",
    anger: "😠",
    fear: "😨",
    surprise: "😲"
};

document.getElementById("result").innerText =
    "Emotion: " + (emoji[data.emotion] || "") + " " + data.emotion +
    " | Intensity: " + data.intensity.toFixed(2);

        document.getElementById("audio").src =
            data.audio + "?t=" + new Date().getTime();
    });
}
</script>

</body>
</html>
"""

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    text = data["text"]

    emotion, intensity = detect_emotion(text)
    audio_path = generate_speech(text, emotion, intensity)

    return jsonify({
        "emotion": emotion,
        "intensity": intensity,
        "audio": audio_path
    })

if __name__ == "__main__":
    app.run(debug=True)