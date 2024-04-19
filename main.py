from fastapi import FastAPI, File, UploadFile
import emotionanalyzer
from fastapi.middleware.cors import CORSMiddleware
import emoanalisis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-audio")
async def upload_file(file: UploadFile = File(...)):
    contenido_archivo = await file.read() 
    text,  emotion, score = emotionanalyzer.getAnalysis(contenido_archivo) 

    return {
                "text": text, 
                "Feel" : emotion,
                "Score" : score
            }

@app.post("/upload-text")
async def upload_file(text):
    emotion = emoanalisis.predict_sentiment(text)
    return {
                "Feel" : emotion    
            }


@app.get("/")
def root():
    return {"messagge" : "Welcome to EmotionsAPI"}

@app.post("/getText")
def getText(text: str):
    return {"El texto introducido fue:" : text}
