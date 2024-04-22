import sttModel 
import emoanalisis


def getAnalysis(audio, key):
    text= sttModel.getSpeechToText(audio, key)
    emotion, score = emoanalisis.predict_sentiment(text) 

    return [text,  emotion, score]