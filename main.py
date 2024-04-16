from fastapi import FastAPI, File, UploadFile
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

@app.get("/")
def root():
    return {"messagge" : "Welcome to EmotionsAPI"}

@app.post("/getText")
def getText(text: str):
    return {"El texto introducido fue:" : text}
