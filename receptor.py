# Imports go at the top
from microbit import *
import radio
import music

def texto_lista(texto):
    return texto.split(",")

'''
    Configuración RADIO
'''
radio.on()
radio.config(channel=3)

#Sienpre en ejecución
while True:
    menssage = radio.receive()
    sleep(20)
    if menssage is not None:
        display.scroll(str(menssage))
