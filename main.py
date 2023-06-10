import win32com.client
import speech_recognition as sr
import webbrowser

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    speaker.Speak(text)


def takeCommand():
    print("Listening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e:
            print("Some error occurred, Sorry")
            return "Could not understand you"


say("I am Jarvis A I")
while 1:
    # s = input()
    s = takeCommand()
    if "Open Youtube".lower() in s.lower():
        webbrowser.open("https://youtube.com")
    say(s)
