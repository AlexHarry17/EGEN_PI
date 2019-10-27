class MotorControl:
    def __init__(self):
        self.move = {'forward': self.move_forward, 'backward': self.move_backward, 'right': self.turn_right, 'left': self.turn_left, 'stop turn': self.stop_turn, 'stop forward/backward': self.stop_forward_reverse}

    def function(self, instruction):
        # Running methods from a dictionary souce: https://stackoverflow.com/questions/36849108/calling-a-function-from-within-a-dictionary, user: alecxe
        self.move[instruction]()

    def move_forward(self):
        print("moving forward")

    def move_backward(self):
        print("moving backward")

    def turn_right(self):
        print("turn right")


    def turn_left(self):
        print("turn left")

    def stop_turn(self):
        print('stop turn')

    def stop_forward_reverse(self):
        print(' stop forward back')