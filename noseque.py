from microbit import *
import speech

n = 1
speech.say('buenardo ,coscu')
forma1 = Image("00000:09090:00000:09990:90009")
forma2 = Image("00000:09090:00000:99999:00000")
forma3 = Image("00000:09090:90009:09990:00000")
forma4 = Image("00000:09090:09090:09990:00000")
forma5 = Image("00000:09990:09990:09990:00000")
forma6 = Image("00000:09990:09990:09990:00000")
while n <= 10:
    display.show(forma1)
    sleep(500)
    display.show(forma2)
    sleep(500)
    display.show(forma3)
    sleep(500)
    display.show(forma4)
    sleep(500)
