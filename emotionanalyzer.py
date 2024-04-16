import sttModel 
import emoanalisis


def getAnalysis(audio):
    
    text = sttModel.getSpeechToText(audio)
    emotion = emoanalisis.predict_sentiment(text) 

    return [text, emotion]