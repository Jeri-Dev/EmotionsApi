from fastapi import FastAPI, File, UploadFile
import emotionanalyzer
from fastapi.middleware.cors import CORSMiddleware
import emoanalisis
import sttModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-audio")
async def upload_file(file: UploadFile = File(...), key: str = ""):
    contenido_archivo = await file.read() 
    text,  emotion, score = emotionanalyzer.getAnalysis(contenido_archivo, key) 

    return {
                "text": text, 
                "Feel" : emotion,
                "Score" : score
            }

@app.post("/upload-text")
async def upload_file(text):
    emotion, score  = emoanalisis.predict_sentiment(text)
    return {
                "Feel" : emotion ,
                "Score" : score   
            }


@app.post("/transcription")
async def transcription(text):
    transcription  = sttModel.getSpeechToText(text)
    return {
                "Transcription" : transcription ,
            }

@app.get("/")
def root():
    return {"messagge" : "Welcome to EmotionsAPI"}

