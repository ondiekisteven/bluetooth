from bluetooth import *

# Create the client socket
client_socket=BluetoothSocket( RFCOMM )

client_socket.connect(("CC:2D:83:12:EA:B5", 3))

client_socket.send("Hello World")

print "Finished"

client_socket.close()