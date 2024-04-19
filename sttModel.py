from google.cloud import speech_v1p1beta1 as speech
import io

#creacion del cliente
client = speech.SpeechClient.from_service_account_file('key.env.json')

#leyendo el archivo de audio
def getSpeechToText(audio):
    #guardando el audio en un formato manejable por la api
    audio_file = speech.RecognitionAudio(content=audio)

    #seteo de configuraciones de la api
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=48000,
        language_code='en-US',
        enable_speaker_diarization=True,
        diarization_speaker_count=2
    )   

    #variable del texto
    response = client.recognize(config = config, audio = audio_file)
    result= response.results[-1]

    word_info = result.alternatives[0].words


    
    speaker_transcript = ""

    for word in word_info:
            speaker_transcript += " " + word.word

    # Imprime la transcripción del Speaker 1
    return speaker_transcript




