from pygame import mixer
import time

mixer.init()
mixer.music.load('audio.mp3')
mixer.music.play()
time.sleep(2)