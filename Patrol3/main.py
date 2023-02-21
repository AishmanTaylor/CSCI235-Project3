#!/usr/bin/env pybricks-micropython
import lib
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Color
from pybricks.ev3devices import (Motor, TouchSensor, UltrasonicSensor)

ev3 = EV3Brick()
ev3.screen.clear()
ev3.screen.draw_text(0, 0, "Patrol3")

# def check_contactLeft(robot):
#     if lib.too_close(robot) and robot.turnedLeftLast:
#         return lib.go_left, check_clear
#     elif lib.left_buttonPressed(robot) and robot.turnedLeftLast:
#         robot.left.reset_angle(BACK_UP_DIST)
#         return lib.left_buttonPressed, check_clear
#     elif lib.right_buttonPressed(robot) and not robot.turnedLeftLast:
#         robot.right.reset_angle(BACK_UP_DIST)
#         return lib.right_buttonPressed, check_clear

# def check_contactRight(robot):
#     if lib.too_close(robot) and not robot.turnedLeftLast:
#         return lib.go_right, check_clear
#     elif lib.left_buttonPressed(robot) and not robot.turnedLeftLast:
#         robot.left.reset_angle(BACK_UP_DIST)
#         return lib.left_buttonPressed, check_clear
#     elif lib.right_buttonPressed(robot) and  robot.turnedLeftLast:
#         robot.right.reset_angle(BACK_UP_DIST)
#         return lib.right_buttonPressed, check_clear

# def check_clear(robot):
#     if robot.light.color() == Color.WHITE:
#         if not lib.too_close(robot) and robot.turnedLeftLast:
#             return lib.go_forward, check_contactLeft
#         elif not lib.too_close(robot) and not robot.turnedLeftLast:
#             return lib.go_forward, check_contactRight
#     elif robot.light.color() != Color.WHITE:
#         return lib.go_back, check_clear

# def reset(robot):
#     distance_turned  = robot.left.angle()
#     if distance_turned != (460):
#         return lib.go_back, check_clear

def patrol(robot):
    if robot.light.color() == Color.WHITE:
        return lib.go_forward, patrol
    elif robot.light.color() != Color.WHITE:
        return lib.go_right, reset
    elif lib.too_close(robot) or lib.left_buttonPressed(robot) or lib.right_buttonPressed(robot):
        return lib.go_left, sonar_check

def sonar_check(robot):
    if lib.too_close(robot):
        return lib.go_left, sonar_check
    return lib.go_forward, patrol

def reset(robot):
    distance_turned  = robot.left.angle()
    if distance_turned == (460):
        return lib.reset_angle, patrol

lib.executor(lib.SensorMotor(ev3), lib.go_forward, patrol)