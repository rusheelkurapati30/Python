#Python program to implement server side of chat room. 

import socket

print("Setup Server...")

server = socket.socket()
print("\nSocket Created")

host_name = socket.gethostname()

print(host_name)

ip = socket.gethostbyname(host_name)
print(ip)

server.bind((ip, int(input("\nEnter port number: "))))

name = input("\nEnter name: ")
server.listen(2)

print("\nWaiting for connection")

connection, address = server.accept()

print("\nConnected with ", address)
clientName = connection.recv(1024).decode()
print(clientName + " has connected.")
print("Press 'bye' to leave the chat room")
connection.send(name.encode())
while True:
	print(name + " > ", end = '')
	serverMessage = input()
	if serverMessage == "bye":
		serverMessage = "Good Night..."
		connection.send(serverMessage.encode())
		print("\n")
		break
	else:
		connection.send(serverMessage.encode())
		clientMessage = connection.recv(1024).decode()
		print(clientName + ">" + clientMessage, end = '')

connection.close()
server.close()






































#11111
# import socket

# server = socket.socket()
# print("\nSocket Created\n")

# server.bind(('localhost', 9999))

# server.listen(3)
# print("\nWaiting for connections")

# while True:
# 	client, addr = server.accept()
# 	name = client.recv(1024).decode()

# 	print("Connected with ", addr, name)

# 	client.send(bytes("\nWelcome " + name, 'utf-8'))

# 	print("\nType [exit] to exit.")
# 	while True:
# 		serverMessage = input("server>>")
# 		if serverMessage != 'exit':
# 			client.send(bytes(serverMessage, 'utf-8'))
# 		message1 = client.recv(1024).decode()
# 		print(name +" > " + message1)


# client.close()









#222222
# import socket

# server = socket.socket()
# # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# print("\nSocket Created\n")

# server.bind(('localhost', 9999))
# # server.bind((socket.gethostname(), 9999))

# server.listen(3)
# print("\nWaiting for connections")

# while True:
# 	client, address = server.accept()
# 	# name = client.recv(4).decode()

# 	# print("Connected with ", address, name)
# 	print(f"Conection from {address} has been established!")

# 	client.send(bytes("\nWelcome to the server!", 'utf-8'))

# 	client.close()

