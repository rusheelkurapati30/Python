#Python server to Java client single server-single client 
# import socket
# soc = socket.socket()
# host_name = socket.gethostname()
# ip = socket.gethostbyname(host_name)
# print(ip)
# port = 5000
# soc.bind((ip, int(port)))
# print("\nWaiting for connection")
# soc.listen(5)
# conn, addr = soc.accept()
# print("Got connection from",addr)
# while True:
# 	length_of_message = int.from_bytes(conn.recv(2), byteorder = 'big')
# 	msg = conn.recv(length_of_message).decode("UTF-8")
# 	print("Client > " + msg)
# 	serverMsg = input("Server > ")
# 	message_to_send = serverMsg.encode("UTF-8")
# 	conn.send(len(message_to_send).to_bytes(2, byteorder = 'big'))
# 	conn.send(message_to_send)

# conn.close()
# soc.close()




#Python program to implement server side of chat room with multiple clients. 

import threading
import socket
host = '192.168.0.125'
port = 3233
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, int(port)))
server.listen(5)
clients = []
aliases = []


def broadcast(message):
    for client in clients:
        # client.send(message)
        client.send(len(message).to_bytes(2, byteorder = 'big'))
        client.send(message)
	
def handle_client(client):
	while True:
		try:
			length_of_message = int.from_bytes(client.recv(2), byteorder = 'big')
			message = client.recv(1024).decode("utf-8")
			broadcast(message)
		except:
			index = client.index(client)
			clients.remove(client)
			client.close()
			alias = aliases[index]
			broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
			aliases.remove(alias)
			break

def receive():
	while True:
		print("server is running and listening...")
		client, address = server.accept()
		print(f'connection is established with {str(address)}')
		# msg = 'name'
		# nameMsg = msg.encode('utf-8')
		# client.send(len(nameMsg).to_bytes(2, byteorder = 'big'))
		# print(nameMsg)
		# client.send(nameMsg)
		length_of_message = int.from_bytes(client.recv(2), byteorder = 'big')
		alias = client.recv(1024).decode('utf-8')
		aliases.append(alias)
		clients.append(client)
		print("clients: " + str(clients) + ", names: " + str(aliases))
		print(f'{alias} has connected to the chat room'.encode('utf-8'))
		connected = 'you are now connected!'.encode('utf-8')
		client.send(len(connected).to_bytes(2, byteorder = 'big'))
		client.send(connected)

		thread = threading.Thread(target = handle_client, args=(client,))
		thread.start()

if __name__ == "__main__":
	receive()





