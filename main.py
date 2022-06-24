from pygame import mixer
from time import sleep

mixer.init()
mixer.music.load("/home/mohamad/projects/python_projects/starter_gaming/jarvis-welcome-back-sir-jarvis-voice.mp3")
mixer.music.set_volume(0.9)
mixer.music.play()

sleep(20)
mixer.music.stop()