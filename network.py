import socket
import base64
from motor_control import MotorControl
class Network:
   def __init__(self):
      #code to get host socket source: http://net-informations.com/python/net/ipadress.htm
      UDP_IP = socket.gethostbyname(socket.gethostname())
      UDP_PORT = 0
# Code for connecting over wifi source: https://wiki.python.org/moin/UdpCommunication
      self.app_socket = socket.socket(socket.AF_INET, # Internet
                           socket.SOCK_DGRAM) # UDP
      self.app_socket.bind((UDP_IP, UDP_PORT))
      print("Port: ", str(self.app_socket).split(',')[5].replace(')>', ''))
      self.get_data(MotorControl())
      app_socket.close()

   def get_data(self, motor_control):

      while True:
         data, addr = self.app_socket.recvfrom(1024) # buffer size is 1024 bytes
	 # Source to decode data from https://stackoverflow.com/questions/35673809/convert-file-to-base64-string-on-python-3, user: tdelaney
         data = data.decode('ascii')
         motor_control.function(data)


Network()
