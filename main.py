from flask import Flask, request, send_file, redirect, url_for, jsonify
from flasgger import Swagger

import speech_recognition as sr
import moviepy.editor as mp
import yt_dlp
import time

app = Flask(__name__)
Swagger(app)


@app.get("/")
def home():
    return redirect(url_for("flasgger.apidocs"))


@app.post("/transcrever")
def transcribe():
    """
    Transcrever vídeo
    ---
    consumes:
      - multipart/form-data
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: Vídeo para realizar transcrição
    responses:
      200:
        description: Transcrição
        examples:
          application/json: { "text": "Texto do vídeo" }
    """

    file = request.files["file"]

    path_file = f"uploads/{file.filename}"

    file.save(path_file)

    video = mp.VideoFileClip(path_file)

    audio = video.audio

    audio.write_audiofile("uploads/temp.wav")

    with sr.AudioFile("uploads/temp.wav") as source:

        recog = sr.Recognizer()

        audio_data = recog.record(source)

        text = recog.recognize_google(audio_data, language="pt-BR")
        return {"text": text}


@app.get("/<yt_id>")
def download(yt_id):

    url = f'https://www.youtube.com/watch?v={yt_id}'

    file_name = f"{int(time.time())}.mp4"

    ydl_opts = {"format": "best", "outtmpl": file_name}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return    send_file(file_name, as_attachment=True)
    
