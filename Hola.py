# Imports go at the top
from microbit import *


# Variable contador
cont = 0

nombre="PETER"

while True:
    display.scroll(nombre)

    if button_a.was_pressed():
        cont = cont + 1
    if button_b.was_pressed():
        cont = cont - 1
        
    display.scroll(cont)
