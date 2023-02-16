#!/usr/bin/env pybricks-micropython
import lib
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.ev3devices import (Motor, TouchSensor, UltrasonicSensor)

ev3 = EV3Brick()
ev3.screen.clear()
ev3.screen.draw_text(0, 0, "Patrol1")

def patrol(robot):
    return lib.go_forward, turn_180

def turn_180(robot):
    distance_traveled  = robot.right.angle()
    if distance_traveled == 4000:
        return lib.go_right, reset

def reset(robot):
    distance_turned  = robot.left.angle()
    if distance_turned == (460):
        return lib.reset_angle, patrol
    
lib.executor(lib.SensorMotor(ev3), lib.go_forward, patrol)