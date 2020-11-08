# from tkinter import *
# from tkinter import ttk

# root = Tk()

# #Creating a Label Widge
# myLabel = Label(root, text = "Hello World!")
# # Showing it onto the screen 
# myLabel.pack()

# root.mainloop()





#Positioning with tkinter's grid system.

# from tkinter import *
# from tkinter import ttk

# root = Tk()

# myLabel1 = Label(root, text="This is text 1")
# myLabel2 = Label(root, text="This is text 2 but the widgit will expand upto the size of the largest text")

# myLabel1.grid(row = 0, column = 0)
# myLabel2.grid(row = 1, column = 1)

# root.mainloop()





# Creating buttons with tkinter.

# from tkinter import *
# from tkinter import ttk

# root = Tk()
# myLabel1 = Label(root, text="This is text 1")
# def myclick():
# 	myLabel = Label(root, text = "Look! I clicked a Button!!")
# 	myLabel.pack()

# myButton = Button(root, text = "Click Me!", command = myclick, fg = "blue", bg = "gray") #state = "disable", padx = "50", pady = "50")

# myButton.pack()

# root.mainloop()





#Creating input fields with tkinter.

# from tkinter import *
# from tkinter import ttk

# root = Tk()

# e = Entry(root, width = 45, bg = "white", fg = "black")
# e.pack()
# e.insert(0, "Enter your name")

# def myClick():
# 	hello = "Hello " + e.get()
# 	myLabel = Label(root, text = hello)
# 	myLabel.pack()

# myButton = Button(root, text = "click me!", command = myClick)
# myButton.pack()

# root.mainloop()





# Building a simple Calculator App.

# from tkinter import *
# from tkinter import ttk

# root = Tk()

# e = Entry(root, width = 50, borderwidth = 5)
# e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
# # e.pack()

# def buttonClick(number):
# 	current = e.get()
# 	e.delete(0, END)
# 	e.insert(0, str(current) + str(number))

# def myclick():
# 	pass

# def buttonClear():
# 	e.delete(0, END)

# def buttonAdd():
# 	firstName = e.get()
# 	global fNum
# 	global math
# 	math = "add"
# 	fNum = int(firstName)
# 	e.delete(0, END)

# def buttonEqual():
# 	secondNumber = e.get()
# 	e.delete(0, END)
# 	if math == "add":
# 		e.insert(0, fNum + int(secondNumber))
# 	if math == "sub":
# 		e.insert(0, fNum - int(secondNumber))
# 	if math == "mul":
# 		e.insert(0, fNum * int(secondNumber))
# 	if math == "div":
# 		e.insert(0, fNum / int(secondNumber))

# def buttonSub():
# 	firstName = e.get()
# 	global fNum
# 	global math
# 	math = "sub"
# 	fNum = int(firstName)
# 	e.delete(0, END)

# def buttonMul():
# 	firstName = e.get()
# 	global fNum
# 	global math
# 	math = "mul"
# 	fNum = int(firstName)
# 	e.delete(0, END)

# def buttonDiv():
# 	firstName = e.get()
# 	global fNum
# 	global math
# 	math = "div"
# 	fNum = int(firstName)
# 	e.delete(0, END)


# button1 = Button(root, text = "1", padx = 45, pady = 22, command = lambda: buttonClick(1))
# button2 = Button(root, text = "2", padx = 45, pady = 22, command = lambda: buttonClick(2))
# button3 = Button(root, text = "3", padx = 45, pady = 22, command = lambda: buttonClick(3))
# button4 = Button(root, text = "4", padx = 45, pady = 22, command = lambda: buttonClick(4))
# button5 = Button(root, text = "5", padx = 45, pady = 22, command = lambda: buttonClick(5))
# button6 = Button(root, text = "6", padx = 45, pady = 22, command = lambda: buttonClick(6))
# button7 = Button(root, text = "7", padx = 45, pady = 22, command = lambda: buttonClick(7))
# button8 = Button(root, text = "8", padx = 45, pady = 22, command = lambda: buttonClick(8))
# button9 = Button(root, text = "9", padx = 45, pady = 22, command = lambda: buttonClick(9))
# button0 = Button(root, text = "0", padx = 45, pady = 22, command = lambda: buttonClick(0))
# buttonAdd = Button(root, text = "+", padx = 44, pady = 22, command = buttonAdd)
# buttonEqual = Button(root, text = "=", padx = 98, pady = 22, command = buttonEqual)
# buttonClear = Button(root, text = "clear", padx = 90, pady = 22, command = buttonClear)
# buttonSub = Button(root, text = "-", padx = 45, pady = 22, command = buttonSub)
# buttonMul = Button(root, text = "x", padx = 44, pady = 22, command = buttonMul)
# buttonDiv = Button(root, text = "/", padx = 44	, pady = 22, command = buttonDiv)

# button1.grid(row = 3, column = 0)
# button2.grid(row = 3, column = 1)
# button3.grid(row = 3, column = 2)

# button4.grid(row = 2, column = 0)
# button5.grid(row = 2, column = 1)
# button6.grid(row = 2, column = 2)

# button7.grid(row = 1, column = 0)
# button8.grid(row = 1, column = 1)
# button9.grid(row = 1, column = 2)

# button0.grid(row = 4, column = 0)
# buttonClear.grid(row = 4, column = 1, columnspan = 2)
# buttonEqual.grid(row = 5, column = 1, columnspan = 2)
# buttonAdd.grid(row = 5, column = 0)

# buttonSub.grid(row = 6, column = 0)
# buttonMul.grid(row = 6, column = 1)
# buttonDiv.grid(row = 6, column = 2)

# myButton = Button(root, text = "Calculate...", command = myclick)

# root.mainloop()































# import tkinter
# tkinter._test()


# from tkinter import *
# from tkinter import ttk
# root = Tk()
# ttk.Button(root, text="Hello World").grid()
# root.mainloop()