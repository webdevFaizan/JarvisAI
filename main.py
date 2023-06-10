import win32com.client
import speech_recognition as sr
import webbrowser
import os
import subprocess

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def open_music_file(file_path):
    if os.path.exists(file_path):
        if os.name == 'nt':
            subprocess.run(['start', file_path], shell=True)
        elif os.name == 'posix':
            subprocess.run(['xdg-open', file_path])
        else:
            print("Unsupported OS. Cannot open the file.")
    else:
        print("File not found.")


def open_app(software_path):
    if os.path.exists(software_path):
        if os.name == 'nt':
            subprocess.run(['start', software_path], shell=True)
        elif os.name == 'posix':
            subprocess.run([software_path])
        else:
            print("Unsupported OS. Cannot open the software.")
    else:
        print("Software not found.")

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
            return "Could not understand you, sorry"


say("I am Jarvis A I")
while 1:
    flag = 1
    # s = input()
    s = takeCommand()
    sites = [["youtube", "https://www.youtube.com"], ["twitter", "https://www.twitter.com"], ["instagram", "https://www.instagram.com"], ["facebook", "https://www.facebook.com"]]

    if "play music" in s.lower():
        musicPath = "C:/Users/XORPIAN/Desktop/Svartalfheim.mp3"
        # musicPath = "O:/Eevergren music ever/New Best/Ragnarok/Svartalfheim _ God of War Ragnarök (Original Soundtrack) ft. Eivør (128 kbps).mp3"
        # musicPath = '/path/to/your/music/file.mp3'
        open_music_file(musicPath)
        say(f"Playing Svartlefiem sir...")
        flag = 0
        # os.system(f"open {musicPath}")
    elif "hello" in s.lower():
        appPath = "C:/Program Files (x86)/Everything/Everything.exe"
        open_app(appPath)
        say(f"Opening Everything sir...")
        flag = 0

    for site in sites:
        if f"Open {site[0]}".lower() in s.lower():
            say(f"Opening {site[0]} sir...")
            webbrowser.open(f"{site[1]}")
            flag = 0
    if flag == 1:
        say(s)

