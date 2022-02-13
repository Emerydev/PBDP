import socket
import sys

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("127.0.0.1", 9876))
my_int = 12
my_bytes = my_int.to_bytes(4, sys.byteorder)
my_byte_array = bytearray(my_bytes)
print(my_byte_array)
clientSocket.send(my_byte_array)
