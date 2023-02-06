# Imports go at the top
from microbit import *

i = 0
lista =("Juan Pedro Suárez Velasco, Alvaro Sierra Orozco, Sergio Ruiz Canela, Sergio Ruiz Desena, Jorge Rivera Bernardez, Manuel Lara Rubio, Andres Pequeño, Dani Tambien Pequeño")
while True:
    
    if button_a.was_pressed():
        i = i - 1
        sleep(500)
    elif button_b.was_pressed():
        i = i + 1
        sleep(500)
        
    if i>len(lista)-1:
        i=0
        
