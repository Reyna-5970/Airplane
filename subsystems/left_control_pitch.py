# libraries
import os
import sys

# RPi path
sys.path.insert(0, '/home/reyna/Airplane/subsystems/')

# other files
from servo import Servo

class Left_Control_Pitch():
    
    def __init__(self):
        ### PREPARE PWM ###
        self.servo = Servo()
        self.servo.initialize(16, 7.5)

    def level(self):
        self.servo.run(3.4, 1) # turn towards 90, 1 is rest

    def up(self):
        self.servo.run(2, 1) # turn towards 0

    def down(self):
        self.servo.run(7.5, 1) # turn towards down
