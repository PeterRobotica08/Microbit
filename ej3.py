# Imports go at the top
from microbit import *
import music

while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
        sleep(000)
        music.play(music.ENTERTAINER)
    elif button_b.was_pressed():
        display.show(Image.ANGRY)
        sleep(000)
        music.play(music.DADADADUM)
