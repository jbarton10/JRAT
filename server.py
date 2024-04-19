import socket

#Creating Server Socket
s = socket.socket()

#Getting host name and host IP
LISTENER_HOSTNAME = socket.gethostname()
LISTENER_IP = socket.gethostbyname(LISTENER_HOSTNAME)

#Port for server to be open on
LPORT = 1234


print("Host name is {} Ip is {}".format(LISTENER_HOSTNAME,LISTENER_IP))

#Binding server 
s.bind((LISTENER_IP,LPORT))

s.listen()