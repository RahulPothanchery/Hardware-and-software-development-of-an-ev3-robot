#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


ev3 = EV3Brick()
left_wheel = Motor(Port.D)
right_wheel = Motor(Port.A)

left_sensor = ColorSensor(Port.S2)
right_sensor = ColorSensor(Port.S3)

robot = DriveBase(left_wheel, right_wheel,wheel_diameter=55,axle_track = 126)
speed = 65
turnproportion = 3
# Write your program here.
while True:
    left_intensity = left_sensor.reflection()
    right_intensity = right_sensor.reflection()
    
    if left_intensity > 93 & right_intensity > 93:
        robot.drive(speed,0)
       
    if right_intensity < 94:
        rightdeviation = 86 - right_intensity
        turn_rate = turnproportion * rightdeviation
        robot.drive(speed,turn_rate)
    elif left_intensity < 90:
        leftdeviation = 86 - left_intensity
        turn_rate = -turnproportion * leftdeviation
        robot.drive(speed,turn_rate)
    else:
        robot.drive(speed,0)        

    
