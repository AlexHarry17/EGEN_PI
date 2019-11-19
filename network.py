import socket
import base64
from motor_control import MotorControl
import stats
import threading
class Network:
   def __init__(self):
      UDP_IP = socket.gethostbyname(socket.gethostname()) # Get ip source: https://stackoverflow.com/questions/48606440/get-ip-address-from-python, user: An0n
      UDP_PORT = 0
   # Code for connecting over wifi source: https://wiki.python.org/moin/UdpCommunication
      self.app_socket = socket.socket(socket.AF_INET, # Internet
                           socket.SOCK_DGRAM) # UDP
      self.app_socket.bind((UDP_IP, UDP_PORT))
      port = int(str(self.app_socket).split(',')[5].replace(')>', ''))

      stats.display(UDP_IP, str(port))

      print("Port: ", port)
      # self.send_network_info(UDP_IP,port)
      self.get_data(MotorControl())
      self.app_socket.close()

   def get_data(self, motor_control):
      while True:
         data, addr = self.app_socket.recvfrom(4096) # buffer size is 1024 bytes
         # Source to decode data from https://stackoverflow.com/questions/35673809/convert-file-to-base64-string-on-python-3, user: tdelaney
         data = data.decode('ascii')
         motor_control.function(data)

   def send_network_info(self,ip,port):
      while True:
         print('sending on port ', port)
         self.app_socket.sendto(b"test", (ip, port))

Network()