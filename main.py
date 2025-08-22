import pyperclip as p_clip
import time
import gtts
from playsound import playsound

previous = ""
try:
    while True:
        current = p_clip.paste()
        if current != previous:
            if current:
                tts = gtts.gTTS(current, lang='en', tld='co.uk')
                tts.save("tts.mp3")
                playsound("tts.mp3") 

            previous = current
        time.sleep(0.5)  

except KeyboardInterrupt:
    print("\nStopped by user.")
