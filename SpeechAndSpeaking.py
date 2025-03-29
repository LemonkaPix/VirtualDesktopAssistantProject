import speech_recognition as sr
import pyttsx3


#region Speech Recognition
r = sr.Recognizer()

def recordText():
    print("Listening..")
    while 1:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                MyText = r.recognize_google(audio, language="pl-PL")
                return MyText

        except sr.RequestError as e:
            print(f"Could not request results: {e}")

        except sr.UnknownValueError:
            # print("Unknown error occurred")
            pass

#endregion

#region Speaking Text
def SpeakText(command):
    print(command)
    engine = pyttsx3.init()

    rate = 190
    engine.setProperty('rate', rate)

    volume = 1.0
    engine.setProperty('volume', volume)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(command)
    engine.runAndWait()
#endregion