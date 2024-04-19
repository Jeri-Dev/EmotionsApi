import sttModel 
import emoanalisis
import io


def getAnalysis(audio):
    
    text= sttModel.getSpeechToText(audio)
    emotion, score = emoanalisis.predict_sentiment(text) 

    print(text)
    return [text,  emotion, score]