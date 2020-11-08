#Python program to perform CRUD Operations with JSON file.

fieldsList = ["ID", "Name", "Age", "Salary"]

JSON_DATABASE = "jsonData.json"

def create():
	global dictionaryValues
	# print(type(database))
	dictionaryValues = []
	status = 'A'
	dictionaryValues.append(status)
	print(fieldsList)
	for countOfFields in range(len(fieldsList)):
		employeeData = input("\nEnter " + fieldsList[countOfFields] + ": ")
		dictionaryValues.append(employeeData)		
	database["data"].append(dictionaryValues)
	saveDataIntoFile()
	select = input("\nDo you want to continue? [y/n] ")
	if (select.upper() == 'Y'):
		create()

def display():
	recordFound = 0
	for record in database['data']:
		if record[0] == "A":
			recordFound += 1
			print("\nEmployee record " + str(recordFound) + ": \n")
			for index in range(len(fieldsList)):
					print(fieldsList[index] + ": " + str(record[index + 1]))
	if recordFound == 0:
		print("\nNo records found.\n")

def search():
	modify("search")


def update():
	modify("update")


def delete():
	modify("delete")
	

def modify(mode):
	recordFound = 0
	searchId = input("\nEnter " + fieldsList[0] + " to " + mode + ": ")
	for record in database['data']:
		if (searchId == record[1]) and (record[0] == "A"):
			recordFound += 1
			print()
			if mode == 'update':
				for index in range(1, len(fieldsList)):
					print(str(index) + ". update " + fieldsList[index])
				select = int(input("\nEnter your choice: "))
				record[select + 1] = input("\nUpdate " + fieldsList[select] + ": ")
				print("\nRecord updated.\n")
			elif mode == 'delete':
				record[0] = "I"
				print("\nRecord deleted.\n")
			else:
				for index in range(len(fieldsList)):
					print(fieldsList[index] + ": " + str(record[index + 1]))
			saveDataIntoFile()

	if recordFound == 0:
		print("\nInvalid ID.\n")


def saveDataIntoFile():
	File = open(JSON_DATABASE, "w")
	File.write(str(database))
	File.close()


def saveDataFromFile():
	global database
	database = {'data': []}
	try: 
		File = open(JSON_DATABASE, "r")
		database = eval(File.read())
		File.close()
	except: 
		File = open(JSON_DATABASE, "w")
		File.close()

saveDataFromFile()

def showMenu():
	while True:
		print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
		print("Please choose: \n1. New employee\n2. Show all employees\n3. search.\n4. Update.\n5. delete.\n6. exit\n")
		print("-" * 55)
		[create, display, search, update, delete, exit][int(input("\nEnter your choice: ")) - 1]()
	

showMenu()







































# #Python program to perform CRUD Operations with JSON file.

# fieldsList = ["ID", "Name", "Age", "Salary"]

# JSON_DATABASE = "jsonData.json"

# def create():
# 	global dictionaryValues
# 	dictionaryValues = {}
# 	fieldsList.insert(0, "status")
# 	dictionaryValues[fieldsList[0]] = "active"
# 	for index in range(1, len(fieldsList)):
# 		dictionaryValues[fieldsList[index]] = input("\nEnter " + fieldsList[index] + ": ")
# 		dictionaryCopy = dictionaryValues.copy()		
# 	database["data"].append(dictionaryCopy)
# 	saveDataIntoFile()
# 	select = input("\nDo you want to continue? [y/n] ")
# 	if (select.upper() == 'Y'):
# 		create()

# def display():
# 	recordFound = 0
# 	for record in database['data']:
# 		if record['status'] == "active":
# 			recordFound += 1
# 			print("\nEmployee record " + str(recordFound) + ": \n")

# 			for index in range(len(fieldsList)):
# 					print(fieldsList[index] + ": " + record[fieldsList[index]])
# 				# select = int(input("\nEnter your choice: "))
# 				# record[fieldsList[select]] = input("\nUpdate " + fieldsList[select] + ": ")

# 			# for key, value in record.items():
# 			# 	print(key + ": " + value)
# 	if recordFound == 0:
# 		print("\nNo records found.\n")

# def search():
# 	recordFound = 0
# 	searchId = input("\nEnter " + fieldsList[0] + " to search: ")
# 	for record in database['data']:
# 		if record['status'] == "active":
# 			if searchId == record[fieldsList[0]]:
# 				recordFound += 1
# 				for index in range(len(fieldsList)):
# 					print(fieldsList[index] + ": " + record[fieldsList[index]])
# 				# for key, value in record.items():
# 				# 	print(key + ": " + value)
# 	if recordFound == 0:
# 		print("\nNo records found.\n")

# def update():
# 	searchId = input("\nEnter " + fieldsList[0] + " to update: ")
# 	for record in database['data']:
# 		if record['status'] == "active":
# 			if searchId == record[fieldsList[0]]:
# 				print()
# 				for index in range(1, len(fieldsList)):
# 					print(str(index) + ". update" + fieldsList[index])
# 				select = int(input("\nEnter your choice: "))
# 				record[fieldsList[select]] = input("\nUpdate " + fieldsList[select] + ": ")
# 	saveDataIntoFile()

# def delete():
# 	searchId = input("\nEnter " + fieldsList[0] + " to delete: ")
# 	for record in database['data']:
# 		if record['status'] == "active":
# 			if searchId == record[fieldsList[0]]:
# 				record['status'] = "inactive"
# 	saveDataIntoFile()
	


# def saveDataIntoFile():
# 	File = open(JSON_DATABASE, "w")
# 	File.write(str(database))
# 	File.close()

# def saveDataFromFile():
# 	global database
# 	database = {'data': []}
# 	try: 
# 		File = open(JSON_DATABASE, "r")
# 		database = eval(File.read())
# 		File.close()
# 	except: 
# 		File = open(JSON_DATABASE, "w")
# 		File.close()

# saveDataFromFile()

# while True:
# 	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
# 	print("Please choose: \n1. New employee\n2. Show all employees\n3. search.\n4. Update.\n5. delete.\n6. exit\n")
# 	print("-" * 55)
# 	[create, display, search, update, delete, exit][int(input("\nEnter your choice: ")) - 1]()
	













# #Python program to perform CRUD Operations with JSON file.

# fieldsList = ["ID", "Name", "Age", "Salary"]

# JSON_DATABASE = "jsonData.json"

# def create():
# 	global dictionaryValues
# 	dictionaryValues = {}
# 	fieldsList.insert(0, "status")
# 	print(fieldsList)
# 	dictionaryValues[fieldsList[0]] = "active"
# 	continueToCreate()

# def continueToCreate():
# 	for index in range(1, len(fieldsList)):
# 		dictionaryValues[fieldsList[index]] = input("\nEnter " + fieldsList[index] + ": ")
# 		dictionaryCopy = dictionaryValues.copy()		
# 	database["data"].append(dictionaryCopy)
# 	saveDataIntoFile()
# 	select = input("\nDo you want to continue? [y/n] ")
# 	if (select.upper() == 'Y'):
# 		create2()

# def display():
# 	recordFound = 0
# 	for record in database['data']:
# 		if record['status'] == "active":
# 			recordFound += 1
# 			print("\nEmployee record " + str(recordFound) + ": \n")
# 			for index in range(len(fieldsList)):
# 					print(fieldsList[index] + ": " + record[fieldsList[index]])
# 	if recordFound == 0:
# 		print("\nNo records found.\n")

# def search():
# 	modify("search")


# def update():
# 	modify("update")


# def delete():
# 	modify("delete")
	

# def modify(mode):
# 	recordFound = 0
# 	searchId = input("\nEnter " + fieldsList[0] + " to " + mode + ": ")
# 	for record in database['data']:
# 		if (searchId == record[fieldsList[0]]) and (record['status'] == "active"):
# 			recordFound += 1
# 			print()
# 			if mode == 'update':
# 				for index in range(2, len(fieldsList)):
# 					print(str(index) + ". update " + fieldsList[index])
# 				select = int(input("\nEnter your choice: "))
# 				record[fieldsList[select]] = input("\nUpdate " + fieldsList[select] + ": ")
# 				print("\nRecord updated.\n")
# 			elif mode == 'delete':
# 				record['status'] = "inactive"
# 				print("\nRecord deleted.\n")
# 			else:
# 				for index in range(len(fieldsList)):
# 					print(fieldsList[index] + ": " + record[fieldsList[index]])
# 			saveDataIntoFile()

# 	if recordFound == 0:
# 		print("\nInvalid ID.\n")


# def saveDataIntoFile():
# 	File = open(JSON_DATABASE, "w")
# 	File.write(str(database))
# 	File.close()


# def saveDataFromFile():
# 	global database
# 	database = {'data': []}
# 	try: 
# 		File = open(JSON_DATABASE, "r")
# 		database = eval(File.read())
# 		File.close()
# 	except: 
# 		File = open(JSON_DATABASE, "w")
# 		File.close()

# saveDataFromFile()

# def showMenu():
# 	while True:
# 		print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
# 		print("Please choose: \n1. New employee\n2. Show all employees\n3. search.\n4. Update.\n5. delete.\n6. exit\n")
# 		print("-" * 55)
# 		[create, display, search, update, delete, exit][int(input("\nEnter your choice: ")) - 1]()
	

# showMenu()


