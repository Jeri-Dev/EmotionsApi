from fastapi import FastAPI, File, UploadFile
from sttModel import getSpeechToText
import emotionanalyzer

app = FastAPI()

@app.post("/upload-audio")
async def upload_file(file: UploadFile = File(...)):
    contenido_archivo = await file.read()
    text, emotion = emotionanalyzer.getAnalysis(contenido_archivo) 

    return {
                "messagge": text, 
                "Feel" : emotion    
            }


