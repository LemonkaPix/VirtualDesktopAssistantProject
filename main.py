import speech_recognition as sr
import pyttsx3

#region Speech Recognition
r = sr.Recognizer()

def recordText():
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

print("Activated..")

while 1:
    text = recordText()
    print(text)
