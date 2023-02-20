# Imports go at the top
from microbit import *
z=0
lista_numeros = [1,2,3,4,5]
for i in lista_numeros:
    z=z+i
display.scroll(z)
