#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
#Definindo sensor de toque
ts = TouchSensor()
#Desligando as leds
leds = Leds()
leds.all_off()
while True:
    if ts.value(): #SE (valor do sensor de toque for 1)
        leds.set_color(leds.LEFT, leds.RED) #ligar LED da Esquerda COR VERMELHO
        leds.set_color(leds.RIGHT, leds.RED) #ligar LED da Direita COR VERMELHO
        Sound.beep() #Fazer o brick apitar
    else:
        leds.set_color(leds.LEFT, leds.GREEN) #ligar LED da Esquerda COR VERDE
        leds.set_color(leds.RIGHT, leds.GREEN) #ligar LED da Direita COR VERDE

