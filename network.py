import socket
import base64
from motor_control import MotorControl
class Network:
   def __init__(self):
      bluetooth_address = 'B8:27:EB:9B:0D:DF'
      bluetooth_port = 3
   # Code for connecting over wifi source: https://wiki.python.org/moin/UdpCommunication
      self.app_socket = socket.socket(socket.AF_BLUETOOTH, # Internet
                           socket.SOCK_STREAM, socket.BTPROTO_RFCOMM ) # Bluetooth socket connection
      self.app_socket.bind((bluetooth_address, bluetooth_port))
      self.app_socket.listen(1)
      self.get_data(MotorControl())
      self.app_socket.close()

   def get_data(self, motor_control):
      client, address = self.app_socket.accept()
      while True:
         data = client.recv(4096) # buffer size is 1024 bytes
         # Source to decode data from https://stackoverflow.com/questions/35673809/convert-file-to-base64-string-on-python-3, user: tdelaney
         if data:
            data = data.decode('ascii')
            try:
               motor_control.function(data)
            except:
               print("Incorrect Movement")
   def send_network_info(self,ip,port):
      while True:
         print('sending on port ', port)
         self.app_socket.sendto(b"test", (ip, port))

Network()