import subprocess
from gtts import gTTS
import os
bot_message = "Welcome Welcome Welcome"
language = "en"
myobj = gTTS(text=bot_message, lang=language)
myobj.save("welcome.mp3")
print('saved')
# Playing the converted file
os.system( "welcome.mp3")#,'vlc', '--play-and-exit')
