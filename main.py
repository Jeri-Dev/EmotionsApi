from fastapi import FastAPI, File, UploadFile
import emotionanalyzer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/upload-audio")
async def upload_file(file: UploadFile = File(...)):
    contenido_archivo = await file.read()
    text, emotion = emotionanalyzer.getAnalysis(contenido_archivo) 

    return {
                "messagge": text, 
                "Feel" : emotion    
            }

@app.get("/")
def root():
    return {"messagge" : "Welcome to EmotionsAPI"}

@app.get("/getText")
def getText(text: str):
    return {"El texto introducido fue:" : text}
