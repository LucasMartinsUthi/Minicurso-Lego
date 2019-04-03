#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
import math

motorD = LargeMotor('outB')
motorE = LargeMotor('outA')

dCentro = 5.5
rRoda = 3

def odometria(dCentro, rRoda):
    C = 2 * math.pi * dCentro
    c = 2 * math.pi * rRoda
    return C/c


def giraRobo(graus):
    razaoRobo = odometria(dCentro, rRoda)
    motorD.run_to_rel_pos(position_sp=(razaoRobo*graus),speed_sp=900,stop_action="brake")
    motorE.run_to_rel_pos(position_sp=-(razaoRobo*graus),speed_sp=900,stop_action="brake")
    sleep(2)
def planoCartesiano(x,y):
    motorD.run_to_rel_pos(position_sp=(360*x),speed_sp=900,stop_action="brake")
    motorE.run_to_rel_pos(position_sp=(360*x),speed_sp=900,stop_action="brake")
    sleep(2)
    if(y>0):
        giraRobo(90)
        motorD.run_to_rel_pos(position_sp=(360*y),speed_sp=900,stop_action="brake")
        motorE.run_to_rel_pos(position_sp=(360*y),speed_sp=900,stop_action="brake")
        sleep(2)
planoCartesiano(1,2)
