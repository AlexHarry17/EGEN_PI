import gpiozero as gpio
import time
import RPi.GPIO as GPIO          
from time import sleep
# import Raspi_MotorHAT

in1 = 24
in2 = 23
en = 25
in3 = 16
in4 = 20
en2 = 21

temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p=GPIO.PWM(en,40)
p2=GPIO.PWM(en2,40)

p.start(en)
p2.start(en2)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")  

class MotorControl:


    def __init__(self):
        # Controling with gpiozero source: https://gpiozero.readthedocs.io/en/stable/api_output.html
        self.move = {'forward': self.move_forward, 'backward': self.move_backward, 'right': self.turn_right, 'left': self.turn_left, 'stop turn': self.stop_turn, 'stop forward/backward': self.stop_forward_reverse}
        self.drive_motor = gpio.Motor(23,24)
        self.drive_motor_2 = gpio.Motor(20,16)

        self.turn_motor = gpio.AngularServo(0,45,-45)
        # self.mh =Raspi_MotorHAT(addr=0x6F)
        # self.motor_1 = self.mh.getMotor(1)
    def function(self, instruction):
        # Running methods from a dictionary souce: https://stackoverflow.com/questions/36849108/calling-a-function-from-within-a-dictionary, user: alecxe
       self.move[instruction]()

    def move_forward(self):
        self.drive_motor.forward(1) # 1 moves forward, 0 stops motor
        self.drive_motor_2.forward(1) # 1 moves forward, 0 stops motor

        print("moving forward")

    def move_backward(self):
        self.drive_motor.backward(1) # 1 Moves backward, 0 stops motor
        self.drive_motor_2.backward(1) # 1 moves forward, 0 stops motor

        print("moving backward")

    def turn_right(self):# Turns vehicle right
        if self.turn_motor.angle < 45: # Max angle
            self.turn_motor.angle += 1
        print("turn right")


    def turn_left(self): # Turns vehicle left
        if self.turn_motor.angle > -45: # Max angle
            self.turn_motor.angle -= 1

        print("turn left")

    def stop_turn(self):
        print('stop turn')

    def stop_forward_reverse(self): # Stops forward / backward movement
        self.drive_motor.forward(0)
        self.drive_motor.backward(0)
        self.drive_motor_2.forward(0)
        self.drive_motor_2.backward(0)
        print('stop forward back')
