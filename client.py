import socket

#Create socket
s=socket.socket()

#Grab client IP address
CLIENT_IP=socket.gethostbyname(socket.gethostname())

PORT=1234
#IP address for the server
s.connect((CLIENT_IP, PORT))


#Recieving Loop

while True:

    client