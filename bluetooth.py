# file: rfcomm-server.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: simple demonstration of a server application that uses RFCOMM sockets
#
# $Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $
 # Source: https://github.com/karulis/pybluez/blob/master/examples/simple/rfcomm-server.py

from bluetooth import *
import time
from motor_control import MotorControl

motor_control = MotorControl()
server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(('B8:27:EB:9B:0D:DF',PORT_ANY))
server_sock.listen(1)
port = server_sock.getsockname()[1]


print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()

print("Accepted connection from ", client_info)

while True:

    try:
         data = client_sock.recv(1024)

         if data:
            data = data.decode('ascii')
            try:
               motor_control.function(data)
            except:
               print("Incorrect Movement")
    except IOError:
      #   client_sock.close()
      #   server_sock.close()
        server_sock=BluetoothSocket( RFCOMM )
        server_sock.bind(('B8:27:EB:9B:0D:DF',PORT_ANY))
        server_sock.listen(1)

        port = server_sock.getsockname()[1]


        print("Waiting for connection on RFCOMM channel %d" % port)
        client_sock, client_info = server_sock.accept()
        print("Accepted connection from ", client_info)

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")