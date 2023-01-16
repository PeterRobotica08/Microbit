from microbit import *
contador = 0

while True:
    if button_a.get_presses():
        contador = contador + 1
    elif button_b.get_presses():
        contador = contador - 1
    elif pin_logo.is_touched():
        display.scroll("PETER", loop=False)
    else:
        display.show(contador)
       
