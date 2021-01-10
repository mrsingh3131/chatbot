import requests
import speech_recognition as sr
from gtts import gTTS
import os

bot_message = ""
message = ""

while bot_message != 'bye' or bot_message != 'thanks':
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything : ")
        audio = r.listen(source)
        try:
            message = r.recognize_google(audio)
            print("you said : {}".format(message))
        except:
            print("Sorry could not recognize your voice")
    if len(message) == 0:
        continue
    print("Sending message now.....")
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})
    print("Bot: ", end=" ")
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = gTTS(text=bot_message)
    welcome = " "
    myobj.save("welcome.mp3")
    # Playing the converted file
    os.system("welcome.mp3")

