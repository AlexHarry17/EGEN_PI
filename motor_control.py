import gpiozero as gpio
import time
import RPi.GPIO as GPIO          
from time import sleep
from Raspi_PWM_Servo_Driver import PWM

# import Raspi_MotorHAT

# Following code for setting up GPIO Source: https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/
in1 = 24
in2 = 23
en = 25
in3 = 16
in4 = 20
en2 = 21
frequency = 1

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
p=GPIO.PWM(en,frequency)
p2=GPIO.PWM(en2,frequency)
p.start(100.0)
p2.start(100.0)


class MotorControl:
# Source for pwm servo control http://raspberrypiwiki.com/index.php/File:Raspi-MotorHAT-python3.zip
    def __init__(self):
        # Controling with gpiozero source: https://gpiozero.readthedocs.io/en/stable/api_output.html
        self.move = {'forward': self.move_forward, 'backward': self.move_backward, 'right': self.turn_right, 'left': self.turn_left, 'stop turn': self.stop_turn, 'stop forward/backward': self.stop_forward_reverse}
        self.drive_motor = gpio.Motor(24,23)
        self.drive_motor_2 = gpio.Motor(16,20)
        self.pwm = PWM(0x6F)
        self.pwm.setPWMFreq(60)
        self.motor_angle = 370.0
        # self.turn_motor = gpio.AngularServo(0,45,-45)
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
        if self.motor_angle < 404: # Max angle
            self.motor_angle += 0.15
        self.pwm.setPWM(0, 0, int(self.motor_angle))
        # time.sleep(1)
        print("turn right")


    def turn_left(self): # Turns vehicle left
        # if self.turn_motor.angle > -45: # Max angle
            # self.turn_motor.angle -= 1
        if self.motor_angle > 340: # Max angle
            self.motor_angle -= 0.15
        self.pwm.setPWM(0, 0, int(self.motor_angle))

        print("turn left")

    def stop_turn(self):
        print('stop turn')

    def stop_forward_reverse(self): # Stops forward / backward movement
        self.drive_motor.forward(0)
        self.drive_motor.backward(0)
        self.drive_motor_2.forward(0)
        self.drive_motor_2.backward(0)
        print('stop forward back')
