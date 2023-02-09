#!/usr/bin/env pybricks-micropython
import lib
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.ev3devices import (Motor, TouchSensor, UltrasonicSensor)

ev3 = EV3Brick()
ev3.screen.clear()
ev3.screen.draw_text(0, 0, "Avoid2Way")

def check_close(robot):
    if lib.too_close(robot):
        return lib.go_left, check_clear

def check_clear(robot):
    if not lib.too_close(robot):
        return lib.go_forward, check_turn

def check_turn(robot):
    if lib.left_buttonPressed(robot):
        return lib.go_left, check_close
    elif lib.right_buttonPressed(robot):
        return lib.go_right, check_close


# left_motor = Motor(Port.A)
# right_motor = Motor(Port.D)
# left_bumper = TouchSensor(Port.S1)
# right_bumper = TouchSensor(Port.S4)
# ev3sonar = UltrasonicSensor(Port.S2)

# SPEED = 360

# # def leftTurnGoingForward():
# #     left_motor.run(SPEED)
# #     right_motor.run(SPEED)
# #     if ev3sonar.distance() < 150:
# #         leftTurn()

# # def leftTurn():
# #     left_motor.run(0)
# #     right_motor.run(-SPEED)

# # def rightTurnGoingForward():
# #     left_motor.run(SPEED)
# #     right_motor.run(SPEED)
# #     if ev3sonar.distance() < 150:
# #         rightTurn()

# # def rightTurn():
# #     left_motor.run(-SPEED)
# #     right_motor.run(0)

# # while True: 
# #     leftTurnGoingForward()
# #     if left_bumper.pressed():
# #         leftTurnGoingForward()
# #     elif right_bumper.pressed():
# #         rightTurnGoingForward()
