from google.cloud import speech

#creacion del cliente
client = speech.SpeechClient.from_service_account_file('key.json.env')

#leyendo el archivo de audio
def getSpeechToText(audio):
    #guardando el audio en un formato manejable por la api
    audio_file = speech.RecognitionAudio(content=audio)

    #seteo de configuraciones de la api
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=48000,
        language_code='en-US'
    )   

    #variable del texto
    response = client.recognize(config = config, audio = audio_file)
    result = response.results[-1].alternatives[0].transcript

    return result


