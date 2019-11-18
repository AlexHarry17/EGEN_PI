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
# server_sock.bind(('B8:27:EB:9B:0D:DF',PORT_ANY))
server_sock.bind(('',PORT_ANY))

server_sock.listen(100)
port = server_sock.getsockname()[1]
last_move = 0.0

print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
# client_sock.send(b'1')

# time.sleep(1)

client_sock.settimeout(2)
# client_sock.setblocking(0)
print("Accepted connection from ", client_info)

last_move = 0.0
while True:
#     client_sock.send(b'1')
#     if time.time() - last_move > 3.0:
#         client_sock.close()
#       #   client_sock.close()
#         server_sock.close()
#         server_sock=BluetoothSocket( RFCOMM )
# #         server_sock.bind(('B8:27:EB:9B:0D:DF',PORT_ANY))
#         server_sock.bind(('',PORT_ANY))

#         server_sock.listen(1)

#         port = server_sock.getsockname()[1]


#         print("Waiting for connection on RFCOMM channel %d" % port)
#         client_sock, client_info = server_sock.accept()
# #         client_sock.send(b'1')
# #         time.sleep(1)
#         client_sock.settimeout(2)
#         print("Accepted connection from ", client_info)
    try:
         data = client_sock.recv(4096)

         if data:
            data = data.decode('ascii')
            try:
               motor_control.function(data)
               last_move = time.time()
            except:
               print("Incorrect Movement")
         else:
             client_sock.close()
    except IOError:
        client_sock.close()
      #   client_sock.close()
        server_sock.close()
        server_sock=BluetoothSocket( RFCOMM )
#         server_sock.bind(('B8:27:EB:9B:0D:DF',PORT_ANY))
        server_sock.bind(('',PORT_ANY))

        server_sock.listen(100)

        port = server_sock.getsockname()[1]
            

        print("Waiting for connection on RFCOMM channel %d" % port)
        client_sock, client_info = server_sock.accept()
#         client_sock.send(b'1')

#         time.sleep(1)
        client_sock.settimeout(1)
        print("Accepted connection from ", client_info)


print("disconnected")

client_sock.close()
server_sock.close()
print("all done")
