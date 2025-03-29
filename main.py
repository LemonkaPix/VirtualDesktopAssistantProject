from SpeechAndSpeaking import *
from GeminiCommunication import generate


while 1:
    text = recordText()
    print(text)
    response = generate(text)
    SpeakText(response)
