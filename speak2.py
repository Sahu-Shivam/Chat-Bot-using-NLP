from gtts import gTTS as gt
import pyglet
import time, os

def tts(text, lang):
    myobj = gt(text, lang='en', slow=False)
    filename = "E:\Personal Assistant\\temp.mp3"
    myobj.save(filename)

    music = pyglet.media.load(filename, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(filename)