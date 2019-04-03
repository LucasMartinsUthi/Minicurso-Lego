#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
sound = Sound() #definindo sound como a nossa variável para SOM
sound.speak("FURG BOT EH TOP").wait()
sleep(1)
sound.tone(2000, 1500).wait()
sleep(1)
sound.tone([(500, 1000, 400)] * 3).wait()
sound.tone([(3000, 2000, 400),(800, 1800, 2000)]).wait()

sound.play('musica/anything.wav').wait()
