import socket


#Getting host name and host IP
LISTENER_HOSTNAME = socket.gethostname()
LISTENER_IP = socket.gethostbyname(LISTENER_HOSTNAME)

#Creating Server Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Port for server to be open on
LPORT = 1234



#Binding server 
s.bind((LISTENER_IP,LPORT))

s.listen(5)
print("Listening on {} from {}".format(LISTENER_HOSTNAME,LISTENER_IP))
client_socket, client_addr = s.accept()

print("Client {} has connected on {}".format(client_addr[0], client_addr[1]))

#Message to establish connection
message = "Hello and Welcome".encode()
client_socket.send(message)

#Loop for keeping the listener alive
while True:

    #Command to send to the client
    command2Send = input("enter command for {}>".format(client_addr[0]))
    client_socket.send(str(command2Send).encode())
    #Close the program
    if command2Send.lower() =="exit":
        break
    commandResults = client_socket.recv(1024).decode()
    print(commandResults)
#End connection with client and close server connections
client_socket.close()
s.close()