import win32com.client
import os

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    speaker.Speak(text)
    # os.system(f"say {text}")


while 1:
    print("Enter")
    s = input()
    say(s)
