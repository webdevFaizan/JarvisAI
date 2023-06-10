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
    flag = 1
    # s = input()
    s = takeCommand()
    sites = [["youtube", "https://www.youtube.com"], ["twitter", "https://www.twitter.com"], ["instagram", "https://www.instagram.com"], ["facebook", "https://www.facebook.com"]]
    for site in sites:
        if f"Open {site[0]}".lower() in s.lower():
            say(f"Opening {site[0]} sir...")
            webbrowser.open(f"{site[1]}")
            flag = 0
    if flag == 1:
        say(s)
