# Python program to implement Server side of chat room.

import socket
import threading 

FORMAT = "utf-8"

hostName = socket.gethostname()
print(hostName)
IP = socket.gethostbyname(hostName)
print(IP)
ADDRESS = (IP, int(input("\nEnter Port Number: "))) 

clients = []
names = [] 
  
server = socket.socket() 
server.bind(ADDRESS) 
  
def receiveClients(): 
    
    print("server is working on " + IP) 
      
    server.listen() 
      
    while True: 
        
        connection, address =  server.accept() 
        connection.send("NAME".encode(FORMAT)) 
          
        name = connection.recv(1024).decode(FORMAT) 
          
        names.append(name) 
        clients.append(connection) 
          
        print(f"Name is :{name}") 
          
        broadcastMessage(f"Press 'q' to exit the window\n{name} has joined the chat!".encode(FORMAT)) 
          
        connection.send("Connection successful!".encode(FORMAT)) 
          
        thread = threading.Thread(target = handle, args = (connection, address)) 
        thread.start() 
          
        print(f"active connections {threading.activeCount()-1}") 
  
def handle(connection, address): 
    
    print(f"new connection {address}") 
    connected = True
      
    while connected: 
        message = connection.recv(1024) 
          
        broadcastMessage(message) 
      
    connection.close() 
  
def broadcastMessage(message): 
    for client in clients: 
        print(client)
        client.send(message) 
  
receiveClients() 















































# import socket 
  
# import threading 
  
# PORT = 7006
  
# SERVER = socket.gethostbyname(socket.gethostname()) 
# # print(server)
# ADDRESS = (SERVER, int(PORT)) 
  
# FORMAT = "utf-8"
  
# clients, names = [], [] 
  
# server = socket.socket() 
# server.bind(ADDRESS) 
  
# def receiveClients(): 
    
#     print("server is working on " + SERVER) 
      
#     server.listen() 
      
#     while True: 
        
#         connection, address =  server.accept() 
#         connection.send("NAME".encode(FORMAT)) 
          
#         name = connection.recv(1024).decode(FORMAT) 
          
#         names.append(name) 
#         clients.append(connection) 
          
#         print(f"Name is :{name}") 
          
#         broadcastMessage(f"{name} has joined the chat!".encode(FORMAT)) 
          
#         connection.send('Connection successful!'.encode(FORMAT)) 
          
#         thread = threading.Thread(target = handle, 
#                                   args = (connection, address)) 
#         thread.start() 
          
#         print(f"active connections {threading.activeCount()-1}") 
  
# def handle(connection, address): 
    
#     print(f"new connection {address}") 
#     connected = True
      
#     while connected: 
#         message = connection.recv(1024) 
          
#         broadcastMessage(message) 
      
#     connection.close() 
  
# def broadcastMessage(message): 
#     for client in clients: 
#         client.send(message) 
  
# receiveClients() 