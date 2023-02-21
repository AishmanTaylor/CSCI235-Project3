#!/usr/bin/env pybricks-micropython
import lib
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Color
from pybricks.ev3devices import (Motor, TouchSensor, UltrasonicSensor)

ev3 = EV3Brick()
ev3.screen.clear()
ev3.screen.draw_text(0, 0, "Patrol1")

def check_contactLeft(robot):
    if lib.too_close(robot) and robot.turnedLeftLast:
        return lib.go_left, check_clear
    elif lib.left_buttonPressed(robot) and robot.turnedLeftLast:
        robot.left.reset_angle(BACK_UP_DIST)
        return lib.left_buttonPressed, check_clear
    elif lib.right_buttonPressed(robot) and not robot.turnedLeftLast:
        robot.right.reset_angle(BACK_UP_DIST)
        return lib.right_buttonPressed, check_clear

def check_contactRight(robot):
    if lib.too_close(robot) and not robot.turnedLeftLast:
        return lib.go_right, check_clear
    elif lib.left_buttonPressed(robot) and not robot.turnedLeftLast:
        robot.left.reset_angle(BACK_UP_DIST)
        return lib.left_buttonPressed, check_clear
    elif lib.right_buttonPressed(robot) and  robot.turnedLeftLast:
        robot.right.reset_angle(BACK_UP_DIST)
        return lib.right_buttonPressed, check_clear

def check_clear(robot):
    if not lib.too_close(robot) and robot.turnedLeftLast:
        return lib.go_forward, check_contactLeft
    elif not lib.too_close(robot) and not robot.turnedLeftLast:
        return lib.go_forward, check_contactRight
    
lib.executor(lib.SensorMotor(ev3), lib.go_forward, patrol)