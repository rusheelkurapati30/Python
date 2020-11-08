#Python program to implement client side of chat room. 

import threading
import socket
import time
alias = input('> Enter your name ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.0.125', 3233))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "name":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()
# time.sleep(1)
send_thread = threading.Thread(target=client_send)
send_thread.start()




