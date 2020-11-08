# Python program to implement Client side of chat room using GUI.

import socket 
import threading 
from tkinter import *
from tkinter import font 
from tkinter import ttk 
  
FORMAT = "utf-8"
  
client = socket.socket() 
  
window = Tk() 
window.withdraw() 
  
login = Toplevel() 
login.title("Login") 
login.resizable(width = False, height = False) 
login.configure(width = 400, height = 300) 

instruction = Label(login, text = "Please login to continue", justify = CENTER) 
instruction.place(relheight = 0.15, relx = 0.4, rely = 0.07) 

labelName1 = Label(login, text = "IP Address: ") 
labelName1.place(x = 62, y = 68) 

ipAddress = Entry(login, width = 30) 
ipAddress.place(relheight = 0.12, relx = 0.35, rely = 0.2)  


labelName2 = Label(login, text = "Port Number: ") 
labelName2.place(x = 59, y = 110) 

portNumber = Entry(login, width = 30)
portNumber.place(relheight = 0.12, relx = 0.35, rely = 0.35) 

labelName3 = Label(login, text = "Your Name: ") 
labelName3.place(x = 59, y = 155) 

userName = Entry(login, width = 30)
userName.place(relheight = 0.12, relx = 0.35, rely = 0.50) 
  
submit = Button(login, text = "Login", command = lambda:verifyConnection()) 
  
submit.place(relx = 0.5, rely = 0.65) 

def verifyConnection(): 
    clientName = userName.get()
    ip = ipAddress.get()
    port = portNumber.get()

    client.connect((ip, int(port))) 
    login.destroy() 
    layout(clientName) 

    rcv = threading.Thread(target = receiveMsg) 
    rcv.start() 

def layout(clientName):     
    global name
    global displayMsgOnWindow, typeMsg
    name = clientName

    window.deiconify() 
    window.title("CHATROOM") 
    window.resizable(width = False,  height = False) 
    window.configure(width = 470, height = 500)

    displayMsgOnWindow = Text(window, width = 20, height = 3, bg = "white", fg = "black", padx = 5, pady = 5, font = 30) 
    displayMsgOnWindow.place(relheight = 0.9, relwidth = 1) 
          
    labelBottom = Label(window, bg = "DimGray",  height = 60) 
    labelBottom.place(relwidth = 1, rely = 0.9) 
         
    typeMsg = Entry(labelBottom, bg = "white", fg = "black", font = 20)  
    typeMsg.place(relwidth = 0.74, relheight = 0.038, rely = 0.009, relx = 0.011)  
    typeMsg.bind("<Return>", displayMsgByClickEnter)

    buttonMsg = Button(labelBottom,  text = "Send", width = 20, bg = "Tomato", command = lambda :sendButton(typeMsg.get())) 
    buttonMsg.place(relx = 0.77, rely = 0.008, relheight = 0.04, relwidth = 0.22) 

    displayMsgOnWindow.config(cursor = "arrow") 
          
    scrollbar = Scrollbar(displayMsgOnWindow) 
    scrollbar.place(relheight = 1, relx = 0.974) 
    scrollbar.config(command = displayMsgOnWindow.yview) 

def displayMsgByClickEnter(event):
    sendButton(typeMsg.get())

def sendButton(textMsg): 
    global msg
    msg = textMsg 
    typeMsg.delete(0, END) 
    snd = threading.Thread(target = sendMessage) 
    snd.start() 
  
def receiveMsg(): 
    while True: 
        try: 
            message = client.recv(1024).decode(FORMAT)    
            if message == 'NAME': 
                client.send(name.encode(FORMAT)) 
            else: 
                displayMsgOnWindow.insert(END, message +"\n\n") 
                displayMsgOnWindow.see(END) 
        except: 
            print("An error occured!") 
            client.close() 
            break 

def sendMessage(): 
    while True: 
        message = (f"{name}: {msg}") 
        client.send(message.encode(FORMAT))     
        break    

def func(event):
    window.destroy()

window.bind("<q>", func)

window.mainloop()




























# import socket 
# import threading 
# from tkinter import *
# from tkinter import font 
# from tkinter import ttk 
  
# FORMAT = "utf-8"
  
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  
  
# window = Tk() 
# window.withdraw() 
  
# login = Toplevel() 
# login.title("Login") 
# login.resizable(width = False, height = False) 
# login.configure(width = 400, height = 300) 
# instruction = Label(login, text = "Please login to continue", justify = CENTER) 
# instruction.place(relheight = 0.15, relx = 0.4, rely = 0.07) 
# labelName = Label(login, text = "IP Address: ") 
# labelName.place(x = 62, y = 68) 

# ipAddress = Entry(login, width = 30) 
# ipAddress.place(relheight = 0.12, relx = 0.35, rely = 0.2)  


# labelName1 = Label(login, text = "Port Number: ") 
# labelName1.place(x = 59, y = 110) 

# portNumber = Entry(login, width = 30)
# portNumber.place(relheight = 0.12, relx = 0.35, rely = 0.35) 

# labelName2 = Label(login, text = "Your Name: ") 
# labelName2.place(x = 59, y = 155) 

# userName = Entry(login, width = 30)
# userName.place(relheight = 0.12, relx = 0.35, rely = 0.50) 
  
# submit = Button(login, text = "Login", command = lambda:verifyConnection()) 
  
# submit.place(relx = 0.5, rely = 0.65) 

# def verifyConnection(): 
#     clientName = userName.get()
#     ip = ipAddress.get()
#     port = portNumber.get()
#     client.connect((ip, int(port))) 
#     login.destroy() 
#     layout(clientName) 
#     rcv = threading.Thread(target = receiveMsg) 
#     rcv.start() 

# def layout(clientName):     
#     global name
#     name = clientName
#     global displayMsgOnWindow, typeMsg
#     window.deiconify() 
#     window.title("CHATROOM") 
#     window.resizable(width = False,  height = False) 
#     window.configure(width = 470, height = 500)

#     displayMsgOnWindow = Text(window, width = 20, height = 3, bg = "white", fg = "black", padx = 5, pady = 5, font = 30) 
#     displayMsgOnWindow.place(relheight = 0.9, relwidth = 1) 
          
#     labelBottom = Label(window, bg = "DimGray",  height = 60) 
#     labelBottom.place(relwidth = 1, rely = 0.9) 
         
#     typeMsg = Entry(labelBottom, bg = "white", fg = "black", font = 20)  
#     typeMsg.place(relwidth = 0.74, relheight = 0.038, rely = 0.009, relx = 0.011)  
          
#     buttonMsg = Button(labelBottom,  text = "Send", width = 20, bg = "Tomato", command = lambda :sendButton(typeMsg.get())) 
#     buttonMsg.place(relx = 0.77, rely = 0.008, relheight = 0.04, relwidth = 0.22) 
          
#     displayMsgOnWindow.config(cursor = "arrow") 
          
#     scrollbar = Scrollbar(displayMsgOnWindow) 
#     scrollbar.place(relheight = 1, relx = 0.974) 
#     scrollbar.config(command =displayMsgOnWindow.yview) 

# def sendButton(textMsg): 
#     global msg
#     msg=textMsg 
#     typeMsg.delete(0, END) 
#     snd= threading.Thread(target =sendMessage) 
#     snd.start() 
  
# def receiveMsg(): 
#     while True: 
#         try: 
#             message = client.recv(1024).decode(FORMAT) 
              
#             if message == 'NAME': 
#                 client.send(name.encode(FORMAT)) 
#             else: 
#                displayMsgOnWindow.config(state = NORMAL) 
#                displayMsgOnWindow.insert(END, message+"\n\n") 
#                displayMsgOnWindow.config(state = DISABLED) 
#                displayMsgOnWindow.see(END) 
#         except: 
#             print("An error occured!") 
#             client.close() 
#             break 

# def sendMessage(): 
#     displayMsgOnWindow.config(state=DISABLED) 
#     while True: 
#         message = (f"{name}: {msg}") 
#         client.send(message.encode(FORMAT))     
#         break    

# window.mainloop()






























