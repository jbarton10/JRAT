import socket

#Create socket
s=socket.socket()

#Grab client IP address
CLIENT_HOSTNAME = socket.gethostname()
CLIENT_IP=socket.gethostbyname(CLIENT_HOSTNAME)

PORT=1234
#IP address for the server
s.connect((CLIENT_IP, PORT))

#Recieving Loop
while True:

    command2Execute = s.recv(1024).decode()