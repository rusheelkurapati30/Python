#Python program to implement client side of chat room. 

import socket

print("\nClient Server...")
client = socket.socket()
client.connect(('192.168.0.125', int(input("\nEnter port number: "))))

name = input("\nEnter Client's name: ")

print("Connected...\n")

client.send(name.encode())

serverName = client.recv(1024).decode()

print(serverName + " has joined...")
print("Enter 'bye' to exit.")

while True:
	serverMessage = client.recv(1024).decode()
	print(serverName, ">", serverMessage)
	clientMessage = input(str("Me > "))
	if clientMessage == "bye":
		clientMessage = "Leaving the Chat room"
		client.send(clientMessage.encode())
		print("\n")
		break
	else:
		client.send(clientMessage.encode())

client.close()






































#1
# import socket

# client = socket.socket()


# client.connect(('localhost', 9999))
# # client.connect((socket.gethostname(), 9999))

# name = input("Enter your name: ")
# client.send(bytes(name, 'utf-8'))

# print(client.recv(1024).decode())


# client.close()

















# while True:
# 	message = client.recv(1024).decode()
# 	print("server > " + message)
# 	while True:
# 		message1 = input("Me > ")
# 		if message1 != exit:
# 			client.send(bytes(message1, 'utf-8'))








#2222222222
# import socket

# client = socket.socket()


# client.connect(('localhost', 9999))
# # client.connect((socket.gethostname(), 9999))

# # name = input("Enter your name: ")
# # client.send(bytes(name, 'utf-8'))

# fullMessage = ''
# while True:
# 	message = client.recv(8)
# 	if len(message) <= 0:
# 		break
# 	else:
# 		fullMessage += message.decode('utf-8')
# print(fullMessage)

# client.close()




#3333333





