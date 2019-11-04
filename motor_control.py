import gpiozero as gpio
import time
class MotorControl:
    def __init__(self):
        # Controling with gpiozero source: https://gpiozero.readthedocs.io/en/stable/api_output.html
        self.move = {'forward': self.move_forward, 'backward': self.move_backward, 'right': self.turn_right, 'left': self.turn_left, 'stop turn': self.stop_turn, 'stop forward/backward': self.stop_forward_reverse}
        self.drive_motor = gpio.Motor(23,24)
        self.turn_motor = gpio.AngularServo(17,45,-45)
    def function(self, instruction):
        # Running methods from a dictionary souce: https://stackoverflow.com/questions/36849108/calling-a-function-from-within-a-dictionary, user: alecxe
       self.move[instruction]()

    def move_forward(self):
        self.drive_motor.forward(1) # 1 moves forward, 0 stops motor
        print("moving forward")

    def move_backward(self):
        self.drive_motor.backward(1) # 1 Moves backward, 0 stops motor
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
        print('stop forward back')
