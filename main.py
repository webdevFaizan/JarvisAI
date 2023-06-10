import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("Enter")
    s = input()
    speaker.Speak(s)
