import assemblyai as aai

def getSpeechToText(FILE, key) :
    aai.settings.api_key = key

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE)

    if transcript.status == aai.TranscriptStatus.error:
        return transcript.error
    else:
        return transcript.text
