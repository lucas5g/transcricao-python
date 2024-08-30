from flask import Flask, request
import speech_recognition as sr 
import moviepy.editor as mp
import time
app = Flask(__name__)

@app.get("/")
def home():
    return "<p>Mostrar o swegger aqui</p>"

@app.post('/transcrever')
def transcribe():
    file = request.files["file"]
    
    # path_file = f"uploads/{int(time.time())}-{file.filename}"
    # path_file = f"uploads/{file.filename}"
    path_file = f"uploads/test.mp4"
    
    print(path_file)
    
    file.save(path_file)
    
    video = mp.VideoFileClip(path_file)

    audio = video.audio
    
    audio.write_audiofile("uploads/test.wav")
        
    with audio as source:
        recog = sr.Recognizer()
        audio_data = recog.record(source)
        
        text = recog.recognize_google(audio_data, language="pt-BR")
        
        return {"text":text}
    

def download(url):
    return 'download o video youtube'