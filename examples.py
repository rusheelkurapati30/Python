 #   print("Rusheel")

# var = "I am Rusheel"
# print(var)

# firstName = "Rusheel"
# lastName  = "Kurapati"
# print(firstName + " " + lastName)

# employees = ["Rusheel", "Raju", "Rakesh"]
# print(employees[0])
# print(employees[-1])
# employees.append("Ramesh")
# print(employees)
# for empList in employees:
# 	print(empList)

# Adding items to a list
# bikes = []
# print(bikes)
# bikes.append("KTM")
# bikes.append("PULSAR")
# print(bikes)

# Making numerical lists
# numbers = []
# for counter in range(1,11):
# 	numbers.append(counter**2)
# 	numbers = [x**2 for x in range(1, 11)]
# 	print(numbers)

# Slicing a list
# employees = ["Rusheel", "Raju", "Rakesh"]
# firstTwo = employees[:2]
# print(firstTwo)

#Copying a list
# employees = ["Rusheel", "Raju", "Rakesh"]
# Copying = employees[:]
# print(Copying)

# employees = ["Rusheel", "Raju", "Rakesh"]
# if "Rusheel" in employees:
# 	print("TRUE")
# else:
# 	print("FALSE")

# age = 18
# if age < 18:
# 	print("Not eligible to vote")
# else:
# 	print("Eligible to vote")	

# bioData = {"Name": "Rusheel", "Age" : 22, "mobileNumber": 8686664502}
# print("Name is " + bioData["Name"])
# # Adding a new key-value pair
# bioData["Address"] = "MOULA-ALI"
# print("Address is: " + bioData["Address"])

# Looping through all key-value pairs
# bioData = {"Name": "Rusheel", "Age" : 22, "mobileNumber": 8686664502}
# for key, value in bioData.items():
# 	print(key + " : " + str(value))

#User input
# name = input("What's your name? ")
# print("Hello, " + name + "!")

#while loop
# counter = 1
# while counter < 5:
# 	print(counter)
# 	counter += 1

# msg = ""
# while msg != "quit":
# 	msg = input("What's your message? ")
# 	print(msg)

# def greet_user():
# 	print("Hello!")
# greet_user()
 
# def name(fullName):
# 	print("Hello, " + fullName + "!")
# name("Rushee Kurapati")

## Default values for parameters
# def make_pizza(topping='bacon'):
#  """Make a single-topping pizza."""
#  print("Have a " + topping + " pizza!")
# make_pizza()
# make_pizza('pepperoni')

##Returning a value
# def addNumers(x, y):
# 	return x + y
# sum = addNumers(8, 3)
# print(sum)

#Creating a dog class
# class Dog():
#  """Represent a dog."""
#  def __init__(self, name):
# 	 self.name = name
#  def sit(self):
#  	print(self.name + " is sitting.")
# my_dog = Dog('Peso')
# print(my_dog.name + " is a great dog!")
# my_dog.sit()

# class car:
# 	def greater():
# 		firstNumber = input("Enter first number: ")
# 		secondNumber = input("Enter second number: ")
# 		if int(firstNumber)> int(secondNumber):
# 			print(firstNumber + " is greater than " + secondNumber)
# 		else:
# 			print(secondNumber + " is greater than " + firstNumber)
# 	greater()

# Writing to a file
# fileName = "names.txt"
# with open(fileName, "w") as fileObject:
# 	name = input("Enter a name: ")
# 	fileObject.write(name)

# Reading a file and storing its lines
# fileName = "names.txt"
# with open(fileName) as fileObject:
# 	lines = fileObject.readlines()
# for line in lines:
# 	print(line.rstrip())

# Appending to a file
# fileName = "names.txt"
# with open(fileName, "a") as fileObject:
#  	name = input("Enter a name: ")
#  	fileObject.write("\n" + name)

# prompt = "How many tickets do you need? "
# num_tickets = input(prompt)
# try:
#  num_tickets = int(num_tickets)
# except ValueError:
#  print("Please try again.")
# else:
#  print("Your tickets are printing.")

#Lists
# employees = ["Rusheel", "Raju", "Rakesh"]
# numOfEmployees = len(employees)
# print(employees[0])
# print(employees[-1])
# employees.append("Dinesh")
# for empList in employees:
# 	print(empList)
# 	#print("welcome")
# ## Length of a list
# numOfEmployees = len(employees)
# print("Length is " + str(numOfEmployees))
# employees.insert(4, "Sonu")
# print(employees)
# employees.sort()
# del employees[-1]
# print(employees)
# employees.sort(reverse=True)
# employees.remove("Rakesh")
# print(employees)
# employees.reverse()
# employees.pop()
# print(employees)
# numOfEmployees = len(employees)
# print("Length is " + str(numOfEmployees))
# ##pop the first element
# employees.pop(0)
# print(employees)

#range()
# for number in range(101):
# 	print(number)

# print("\n")
# for number in range(90, 101):
# 	print(number)

##min(), max(), sum()
# marks = [90, 50, 87, 48]
# minMark = min(marks)
# print(minMark)
# maxMark = max(marks)
# print(maxMark)
# sumOfMarks = sum(marks)
# print(sumOfMarks)

# Using a loop to generate a list of square numbers
# squares = []
# for counter in range(1, 11):
# 	square = counter**2
# 	print(square)

# name = input("Enter a name: ");
# upperCase = name.upper()
# print(upperCase)

# name = input("Enter a name: ")
# lowerCase = name.lower()
# print(lowerCase)

# dogs = []
# dogs.append('willie')
# dogs.append('hootz')
# dogs.append('peso')
# dogs.append('goblin')
# for dog in dogs:
#  print("Hello " + dog + "!")
# print("I love these dogs!")
# print("\nThese were my first two dogs:")
# old_dogs = dogs[:2]
# for old_dog in old_dogs:
#  print(old_dog)
# del dogs[0]
# dogs.remove('peso')
# print(dogs)

## Removing a key value pair.
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

# Store people's favorite languages.
# fav_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
# numOfMembers = len(fav_languages)
# print(numOfMembers)
# Show each person's favorite language.
#for name, language in fav_languages.items():
 #print(name + ": " + language)
#for name in fav_languages.keys():
	#print(name)
# for language in fav_languages.values():
#  	print(language)
#sorted and reverse
# for name, language in sorted(fav_languages.items(), reverse = True):
# 	print(name + ": " + language)

# #Storing dictionaries in a list
# list = []
# newList = {
# 		'firstName': 'Rusheel', 
# 		'lastName': 'Kumar',
# 		}
# list.append(newList)
# newList = {
# 		'firstName': 'Ramu', 
# 		'lastName': 'Kumar',
# 		}
# list.append(newList)
# print(list)

# users = [
#  {
#  'last': 'fermi',
#  'first': 'enrico',
#  'username': 'efermi',
#  },
#  {
#  'last': 'curie',
#  'first': 'marie',
#  'username': 'mcurie',
#  },
# ]
# # Show all information about each user.
# for user_dict in users:
#  for k, v in user_dict.items():
#  		print(k + ": " + v)

# Store multiple languages for each person.
# fav_languages = {
#  'jen': ['python', 'ruby'],
#  'sarah': ['c'],
#  'edward': ['ruby', 'go'],
#  'phil': ['python', 'haskell'],
# }
# # Show all responses for each person.
# for name, langs in fav_languages.items():
# 		print(name + ": " + str(langs))

#Storing dictionaries in a dictionary
# employees = {
# 	"Rusheel": {
# 			"first": "rusheel",
# 			"last": "kumar",
# 			"location": "moula ali"
# 		},
# 	"Ramu": {
# 			"first": "ramu",
# 			"last": "kurapati",
# 			"location": "hanuman nagar"
# 		}
# 	}
# for userName, userDict in employees.items():
# 	print("\nUser name: " + userName)
# 	fullName = userDict["first"] + " "	
# 	fullName += userDict["last"]
# 	location = userDict["location"]
# 	print("\tFull name: " + fullName)
# 	print("\tLocation: " + location)

# aliens = []
# # Make a million green aliens, worth 5 points
# # each. Have them all start in one row.
# for alien_num in range(101):
# 	 new_alien = {}
# 	 new_alien['color'] = 'green'
# 	 new_alien['points'] = 5
# 	 new_alien['x'] = 20 * alien_num
# 	 new_alien['y'] = 0
# 	 aliens.append(new_alien)
# 	 print(aliens)
# # Prove the list contains a million aliens.
# num_aliens = len(aliens)
# print("Number of aliens created:")
# print(num_aliens)

# age = 12
# if age < 4:
#  price = 0
# elif age < 18:
#  price = 5
# else:
#  price = 10
# print("Your cost is $" + str(price) + ".")

# list = ['Rusheel', 'Ramu', 'Raju', Ravi']
# person = 'Ramu'
# if person not in list:
# 		print("False")
# else:
# 		print("True") 

# players = ["Rusheel"]
# if players:
# 		for player in players:
#  			print("Player: " + player)
# else:
# 	print("We have no players yet!") 

#Letting the user choose when to quit
# prompt = "\nTell me something, and I'll "
# prompt += "repeat it back to you."
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
# 	message = input(prompt)
# 	if message != 'quit':
# 		print(message)

# users = ['Rusheel', 'Ravi', 'Ramu']
# prompt = "\nAdd a player to your team."
# prompt += "\nEnter 'quit' when you're done. "
# update = []
# while True:
# 	newUser = input(prompt)
# 	if newUser =='quit':
# 		break
# 	elif newUser in users:
# 		print(newUser + " is already updated.")
# 		continue
# 	else:
# 		update.append(newUser)
# print("\nUsers: ")
# for newUser in users:
# 	print(newUser)

# #Infinite loop
# while True:
# 	name = input("\nWho are you? ")
# 	print("Nice to meet you, " + name + "!")

# names = ['Rusheel', 'Duplicate', 'Raju', 'Duplicate']
# print(names)
# while "Duplicate" in names:
# 	names.remove("Duplicate")
# print(names)

## Functions.
# Making a function.
# def function():
# 	print("Hello!")
# function()

# Passing a single argument.

# def name(fullName):
# 	print(fullName)
# name('Rusheel kurapati')

#Using positional arguments
# def describePet(animal, name):
# 	print("\nI have a " + animal + ".")
# 	print("Its name is " + name + ".")
# describePet('dog', 'peso')
# describePet('peso', 'dog')

#Using keyword arguments
# def describePet(animal, name):
# 	print("\nI have a " + animal + ".")
# 	print("Its name is " + name + ".")
# describePet(name = "peso", animal = "dog")

#Using a default value
# def describe_pet(name, animal='dog'):
#  print("\nI have a " + animal + ".")
#  print("Its name is " + name + ".")
# describe_pet('harry', 'hamster')
# describe_pet('willie')

# Using None to make an argument optional
# def describePet(animal, name=None):
# 	print("\nI have a " + animal + ".")
# 	if name:
# 		print("Its name is " + name + ".")
# describePet('dog', 'peso')
# describePet('dog')

#Returning a single value
# def getFullName(first, last):
# 	fullName = first + " " + last
# 	return fullName
# functionCall = getFullName('Rusheel', 'Kurapati')
# print(functionCall)

# Returning a dictionary
# def build_ person(first, last):
#  person = {'first': first, 'last': last}
#  return person
# musician = build_person('jimi', 'hendrix')
# print(musician)

# Returning a dictionary with optional values
# def build_person(first, last, age=None):
#  person = {'first': first, 'last': last}
#  if age:
#  	person['age'] = age
#  	return person
# musician = build_person('jimi', 'hendrix', 27)
# print(musician)
# musician = build_person('janis', 'joplin')
# print(musician)

# Passing a list as an argument
# def greetUsers(names):
# 	for name in names:
# 		msg = "Hello " + name + "!"
# 		print(msg)
# names = ['rusheel', 'ravi', 'ramu']
# greetUsers(names)

# import json
# numbers = [2, 3, 5, 7, 11, 13]
# jsondump = 'numbers.json'
# with open('jsondump.txt', 'w') as f_obj:
#  json.dump(numbers, f_obj)


# import json
# jsondump = 'numbers.json'
# with open('jsondump.txt') as f_obj:
#  numbers = json.load(f_obj)
# print(numbers)

#2D Lists and Nested loops

# numberGrid = [
# 	[1, 2, 3],
# 	[4, 5, 6],
# 	[7, 8, 9],
# 	[0]
# ]
# for row in numberGrid:
# 	for column in row:
# 		print(column)

# birthYear = input("Birth Year: ")
# age = 2020 - int(birthYear)
# print(age)







# Python program to perform crud operations
# empFields = ["status", "employeeId", "employeeName", "employeeSalary"]
# totalEmployeeData = [['A', 1, "rusheel", 1500],['A', 2, "ravi", 2000],['A', 3, "raju", 2500]]
# status = 'A'
# def create():
# 	newData = []
# 	# File = open("datbaseFile.dat", "a")
# 	noOfRecords = int(input("\nHow many employee records do you want? "))
# 	for record in range(noOfRecords):
# 		print("\nEnter employee " + str(record + 1) + " details: ")
# 		for countOfField in range(len(empFields)):
# 			employeeData = input("\nEnter " + empFields[countOfField] + ": ")
# 			status = 'A'
# 			newData.append(employeeData)
# 		totalEmployeeData.append(newData)	
# 			# File.write(employeeData + "\n")
# 	# File.close()
# 	# print(len(employeeData))
# 	# 	empId = input("Enter employee ID: ")
# 	# 	empName = input("Enter employee Name: ")
# 	# 	empSal = input("Enter employee Salary: ")
# 	# createFile.write(empId + "\n")
# 	# createFile.write(empName + "\n")
# 	# createFile.write(empSal + "\n")
# def read():
# 	for record in totalEmployeeData:
# 		for counter in range(len(empFields)):
# 			print(empFields[counter] + ": " + str(record[counter]))
# 		print()	


















	# try: 
	# 	# File = open("datbaseFile.dat", "r")
	# 	# employeeData = File.readlines()
	# 	# if status == 'A':
	# 		for index in range(len(totalEmployeeData)):
	# 			if index % len(empFields) == 0:
	# 				for counter in range(len(empFields)):
	# 					print(empFields[counter] + " is: " + employeeData[index + counter], end = "")
	# 				print()
	# 		File.close()			
	# except:
	# 	print("\nFile does not exist.\n")		
	# # print("Employee ID is: " + (empDetails))
	# # print("Employee Name is: " + empDetails)
	# # print("Employee Salary is: " + empDetails)
	# # print(f'Name is {name}')

# def update():
# 	counter = 0
# 	searchId = int(input("Enter ID to delete: "))
# 	for record in totalEmployeeData:
# 		if record[1] == searchId:
# 			print("record found.")
# 			totalEmployeeData[counter][0] = 'I'
# 		counter += 1
	# recordFound = 0
	# File = open("datbaseFile.dat", "r")
	# updateId = input("\nEnter Id to update: ")
	# print()
	# # pos = 0
	# employeeData = File.readlines()
	# for index in range(len(employeeData)):
	# 	if updateId in employeeData[index]:
	# # 		new = input("Enter " + employeeData[index] + " to update: ")
	# # 		File.seek(pos)
	# # 		File.write(new)
	# # File.close()
	# 		print(employeeData)
	# print("\n1. Update Name\n2. Update Salary")
	# choice = int(input("Enter your choice: "))
	# if choice == 1:
	# 	employeeData[choice] = input("Enter name to update: ")
	# 	print("name: " + employeeData[choice])
	# 	File.seek(1)
	# 	File.write(employeeData[choice])
	# if choice == 2:
	# 	employeeData[choice] = input("Enter Salary to update: ")
	# 	File.seek(1)
	# 	File.write(employeeData[choice])
	# for index in range(1, len(employeeData)):
	# 	employeeData = input("\nEnter " + empFields[index] + " to update: ")
	# 	File.seek(1)
	# 	File.write(employeeData)
	# # 
	# # 	if updateId in employeeData[index]:
	# # 			# print(len(employeeData))
	# # 			# print(index)
	# # 			# print(len(empFields))
	# # 		# if index % len(empFields) == 0:
	# # 			for counter in range(1, len(empFields)):
	# # 				employeeData[counter] = input("\nEnter " + empFields[counter] + " to update: ")
	# # 				# print(empFields[counter] + " is: " + employeeData[index + counter], end = "")
	# # 				# File.seek()
	# # 				File.write(employeeData)
	# # 			print()
	# File.close()			


	# # 	if updateId in employeeData[index]:
	# # 		recordFound += 1
	# # 		if index % (len(empFields)) == 0:
	# # 			for counter in range(1, len(empFields)):
	# # 				File.seek(3)
	# # 			print("\nUpdated succesfully.\n")	
	# # File.close()

# def delete():
# 	counter = -1
# 	searchId = int(input("Enter ID to delete: "))
# 	for record in totalEmployeeData:
# 		counter += 1
# 		if record[1] == searchId:
# 			print("record found.")
# 			totalEmployeeData[counter][0] = 'I'

# 			# [subl for subl in totalEmployeeData if subl[0] != record[0]]
# 			# for counter in range(len(empFields)):
# 			# 	print(empFields[counter] + ": " + str(record[counter]))
# def search():
# 	searchId = int(input("Enter ID to search: "))
# 	for record in totalEmployeeData:
# 		if record[0] == searchId:
# 			print("record found.")
# 			for counter in range(len(empFields)):
# 				print(empFields[counter] + ": " + str(record[counter]))








	# recordFound = 0
	# File = open("datbaseFile.dat", "r")
	# searchId = input("\nEnter Id to search: ")
	# print()
	# # print(searchId)
	# employeeData = File.readlines()
	# # print(employeeData)
	# for index in range(len(employeeData)):
	# 	# print(index)
	# 	# print(len(employeeData))
	# 	# print(employeeData[index])
	# 	if searchId in employeeData[index]:
	# 		# print("valid")
	# 		recordFound += 1
	# 		if index % len(empFields) == 0:
	# 			for counter in range(len(empFields)):
	# 				# print("%s is: %s" %  (empFields[counter], employeeData[index + counter]), end = "")
	# 				print(empFields[counter] + " is: " + employeeData[index + counter], end = "")
	# 			print()
	# if recordFound == 0:
	# 	print("Invalid ID.\n")
	# 	# break;
	# File.close()		
					

# while True:
# 	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
# 	print("Please choose: \n1. New employee\n2. Show all employees\n3. Update an employee\n4. Delete an employee\n5. Search an employee\n6. exit\n")
# 	print("-------------------------------------------------------\n")
# 	choice = int(input("Enter your choice: "))
# 	if choice == 1:
# 		create()
# 	elif choice == 2:
# 		read()
# 	elif choice == 3:
# 		update()
# 	elif choice == 4:
# 		delete()
# 	elif choice == 5:
# 		search()
# 	elif choice ==6:
# 		exit(0)
# 	else:
# 		print("\nInvalid choice.")

# empId
# empName
# empSal
#Reading a file and storing its lines
# fileName = "names.txt"
# with open(fileName) as fileObject:
# 	lines = fileObject.readlines()
# for line in lines:
# 	print(line.rstrip())


#while True:
# 	name = input("\nWho are you? ")
# 	print("Nice to meet you, " + name + "!")


# fileName = "menu.cfg"
# with open(fileName) as fileObject:
# 	lines = fileObject.readlines()
# while True:
# 	print('\n')
# 	for line in lines:
# 		print(line)

# fileName = open("menu.cfg", "r")
# lines = fileName.readlines()
# while True:
# 	print('\n')
# 	for line in lines:
# 		print(line)
# 	choice = input("Enter your choice: ")
# 	# def switch(choice):
# 	def create():
# 		fileData = open("datbaseFile.dat", "a")
# 		noOfRecords = input("How many records do you want? ")
# 		for record in noOfRecords:
# 			fields = open("fields.cfg", "r")
# 			fieldLines = fields.readlines()
# 			for line in fieldLines:
# 				employeeDetails = input("Enter " + line + ":")
# 				fileData.write(employeeDetails)

# 			fileData.close()
# 				# print(line)
# 	def display():
# 		fileData = open("datbaseFile.dat", "r+")
# 		data = fileData.readlines()
# 		for employeesDetails in data:
# 			print(line + ": " + employeeDetails)
# 		fileData.fclose()	
# 		# return switcher.get(choice, "Invalid choice!")
# fileName.close()

## Functions.
# Making a function.
# def function():
# 	print("Hello!")
# function()

# Passing a single argument.

# def name(fullName):
# 	print(fullName)
# name('Rusheel kurapati')

#Using positional arguments
# def describePet(animal, name):
# 	print("\nI have a " + animal + ".")
# 	print("Its name is " + name + ".")
# describePet('dog', 'peso')
# describePet('peso', 'dog')

#Using keyword arguments
# def describePet(animal, name):
# 	print("\nI have a " + animal + ".")
# 	print("Its name is " + name + ".")
# describePet(name = "peso", animal = "dog")



# fileName = open("menu.cfg", "r")
# lines = fileName.readlines()
# while True:
# 	print('\n')
# 	for line in lines:
# 		print(line)
# 		choice = input("Enter your choice: ")
# 	def switch(choice):
# 		switcher = {
# 		1: create(),
# 		2: display()
# 		}
# 		return switcher.get(choice, "Invalid choice!")
# fileName.close()

# fileName = open("menu.cfg", "r")
# while True:
# 	for line in fileName:
# 		print(line)





# # Python program to perform crud operations
# empFields = ["status", "employeeId", "employeeName", "employeeSalary"]
# totalEmployeeData = []
# recordFound = 0
# # totalEmployeeData = [['A', 1, "rusheel", 1500],['A', 2, "ravi", 2000],['A', 3, "raju", 2500]]
# # status = 'A'

# def create():
	
# 	# File = open("datbaseFile.dat", "a")
# 	noOfRecords = int(input("\nHow many employee records do you want? "))
# 	for record in range(noOfRecords):
# 		newData = []
# 		print("\nEnter employee " + str(record + 1) + " details: ")
# 		for countOfField in range(len(empFields)):
# 			employeeData = input("\nEnter " + empFields[countOfField] + ": ")
# 			# status = 'A'
# 			newData.append(employeeData)
# 		totalEmployeeData.append(newData)
# 	print(totalEmployeeData)

# def read():
# 	recordFound = 0
# 	for record in totalEmployeeData:
# 		if record[0] == 'A':
# 			recordFound +=1
# 			for counter in range(1, len(empFields)):
# 				print(empFields[counter] + ": " + str(record[counter]))
# 			print()	
# 	if recordFound == 0:
# 			print("\nNo records found.\n")
# 			# print("record found")
# 			# for counter in range(len(empFields) - 1):
# 			# 	print(counter)
# 			# 	print(totalEmployeeData[counter])
# 			# 	if totalEmployeeData[counter][0] == 'A':
# 			# 		# print("hi")
# 			# 		# print(empFields[counter] + ": " + str(record[counter]))
# 			# 		print()	

# def update():
# 	counter = 0
# 	searchId = input("Enter ID to update: ")
# 	for record in totalEmployeeData:
# 		recordFound = 0
# 		if record[0] == 'A' and record[1] == searchId:
# 			recordFound += 1
# 			print("record found.")
# 			print("\n1. To update name")
# 			print("2. To update salary")
# 			choice = int(input("\nEnter your choice: "))
# 			if choice == 1:
# 				totalEmployeeData[counter][2] = input("\nEnter name to update: ")
# 				print("\nUpdated successfully.\n")
# 			if choice == 2:
# 				totalEmployeeData[counter][3] = input("\nEnter salary to update: ")
# 				print("\nUpdated successfully.\n")
# 		counter += 1
# 	if recordFound == 0:
# 		print("\nInvalid ID.\n")
	

# def delete():
# 	counter = -1
# 	searchId = input("Enter ID to delete: ")
# 	# print("hi")
# 	for record in totalEmployeeData:
# 		recordFound = 0
# 		print(totalEmployeeData)
# 		counter += 1
# 		if record[0] == 'A' and record[1] == searchId:
# 			recordFound += 1
# 			print("record found.")
# 			# record[0] == 'I'
# 			# for counter in range(1, len(empFields)):
# 			# 	print(totalEmployeeData[counter][0])
# 			totalEmployeeData[counter][0] = 'I'
# 	if recordFound == 0:
# 		print("\nInvalid ID.\n")
# 	else:
# 		print("\nRecord deleted.\n")


# def search():
# 	searchId = input("Enter ID to search: ")
# 	for record in totalEmployeeData:
# 		recordFound = 0
# 		if record[0] == 'A' and record[1] == searchId:
# 			recordFound += 1
# 			print("record found.")
# 			for counter in range(1, len(empFields)):
# 				print(empFields[counter] + ": " + str(record[counter]))
# 	if recordFound == 0:
# 		print("\nInvalid ID.\n")

# while True:
# 	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
# 	print("Please choose: \n1. New employee\n2. Show all employees\n3. Update an employee\n4. Delete an employee\n5. Search an employee\n6. exit\n")
# 	print("-------------------------------------------------------\n")
# 	choice = int(input("Enter your choice: "))
# 	if choice == 1:
# 		create()
# 	elif choice == 2:
# 		read()
# 	elif choice == 3:
# 		update()
# 	elif choice == 4:
# 		delete()
# 	elif choice == 5:
# 		search()
# 	elif choice ==6:
# 		exit(0)
# 	else:
# 		print("\nInvalid choice.")




# from xml.dom import minidom 
# import os  
  
  
# root = minidom.Document() 
  
# xml = root.createElement('root')  
# root.appendChild(xml) 
  
# productChild = root.createElement('product') 
# productChild.setAttribute('name', 'Geeks for Geeks') 
  
# xml.appendChild(productChild) 
  
# xml_str = root.toprettyxml(indent ="\t")  
  
# save_path_file = "gfg.xml"
  
# with open(save_path_file, "w") as f: 
#     f.write(xml_str) 



import xml.etree.ElementTree as gfg  
  
  
def GenerateXML(fileName) : 
      
    root = gfg.Element("Catalog") 
      
    m1 = gfg.Element("mobile") 
    root.append (m1) 
      
    b1 = gfg.SubElement(m1, "brand") 
    b1.text = "Redmi"
    b2 = gfg.SubElement(m1, "price") 
    b2.text = "6999"
      
    m2 = gfg.Element("mobile") 
    root.append (m2) 
      
    c1 = gfg.SubElement(m2, "brand") 
    c1.text = "Samsung"
    c2 = gfg.SubElement(m2, "price") 
    c2.text = "9999"
      
    m3 = gfg.Element("mobile") 
    root.append (m3) 
      
    d1 = gfg.SubElement(m3, "brand") 
    d1.text = "RealMe"
    d2 = gfg.SubElement(m3, "price") 
    d2.text = "11999"
      
    tree = gfg.ElementTree(root) 
      
    with open (fileName, "wb") as files : 
        tree.write(files) 
  
# Driver Code 
if __name__ == "__main__":  
    GenerateXML("Catalog.xml") 