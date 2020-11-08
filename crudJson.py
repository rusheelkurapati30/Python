#Python program to perform CRUD Operations with JSON file.

fieldsList = ["ID", "Name", "Age", "Salary"]

JSON_DATABASE = "jsonData.json"

def create():
	dictionaryValues = {}
	for index in range(len(fieldsList)):
		dictionaryValues[fieldsList[index]] = input("\nEnter " + fieldsList[index] + ": ")
		dictionaryCopy = dictionaryValues.copy()		
	database["data"].append(dictionaryCopy)
	saveDataIntoFile()
	select = input("\nDo you want to continue? [y/n] ")
	if (select == 'y') or (select == 'Y'):
		create()

def display():
	recordFound = 0
	for record in database['data']:
		recordFound += 1
		print("\nEmployee record " + str(recordFound) + ": \n")
		for key, value in record.items():
			print(key + ": " + value)
	if recordFound == 0:
		print("\nNo records found.\n")

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

while True:
	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
	print("Please choose: \n1. New employee\n2. Show all employees\n3. exit\n")
	print("-------------------------------------------------------")
	choice = int(input("\nEnter your choice: "))
	if choice == 1:
		create()
	elif choice == 2:
		display()
	elif choice == 3:
		exit(0)
	else:
		print("\nInvalid choice.")
























#Python program to perform create and read a json file.

empFields = ["Employee ID", "Employee Name", "Employee Salary"]
# mydict = {}
# database = {'data': []}
def create():
	dictionaryValues = {}
	noOfRecords = int(input("\nhow many records do you want? "))
	for record in range(noOfRecords):
		print("\nEnter employee record " + str(record+1) + ": ")
		for index in range(len(empFields)):
			dictionaryValues[empFields[index]] = input("\nEnter " + empFields[index] + ": ")
			dictionaryCopy = dictionaryValues.copy()		
		database["data"].append(dictionaryCopy)

def display():
	recordFound = 0
	for record in database['data']:
		recordFound += 1
		print("\nEmployee record " + str(recordFound) + ": \n")
		for key, value in record.items():
			print(key + ": " + value)
	if recordFound == 0:
		print("\nNo records found.\n")

def exitProgram():
	File = open("jsonData.json", "w")
	File.write(str(database))
	File.close()
	exit(0)

def readDataFromFile():
	global database
	database = {'data': []}
	try: 
		# dictionaryValues = {}
		File = open("jsonData.json", "r")
		database = eval(File.read())
		File.close()
	except: 
		File = open("jsonData.json", "w")
		File.close()

readDataFromFile()

while True:
	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
	print("Please choose: \n1. New employee\n2. Show all employees\n3. exit\n")
	print("-------------------------------------------------------")
	choice = int(input("\nEnter your choice: "))
	if choice == 1:
		create()
	elif choice == 2:
		display()
	elif choice == 3:
		exitProgram()
	else:
		print("\nInvalid choice.")















# fieldKeys = ["ID", "Name", "Age"]
# fieldValues = ["1", "rusheel", "22"]
# newValues = {}
# for index in range(len(fieldKeys)):
# 	newValues[fieldKeys[index ]] = fieldValues[index]
# print(newValues)




# fieldKeys = ["ID", "Name", "Age"]
# fieldValues = ["1", "rusheel", "22"]

# newValue = zip(fieldKeys, fieldValues)
# lispOfTuples = list(newValue)
# convertedDict = dict(lispOfTuples)
# print(convertedDict) 	



# fieldKeys = ["ID", "Name", "Age"]
# fieldValues = []
# for index in range(len(fieldKeys)):
# 	fieldValues = input("\nEnter " + str(fieldKeys[index]) + ": ")
# 	# for i in range(index):
# 		convertedDict = dict(zip(fieldKeys, fieldValues))
# print(convertedDict) 	
# File = open("dictionary.json", "w")
# File.write(str(convertedDict))



# empFields = ["Employee ID", "Employee Name", "Employee Salary", "Employee Age", "Employee Address", "Employee Joining Date", "Employee Mobile Number"]
# recordFound = 0
# totalEmployeeData = {}
# def create():
# 	noOfRecords = int(input("\nHow many employee records do you want? "))
# 	for record in range(noOfRecords):
# 		newData = []
# 		# status = 'A'
# 		# newData.append(status)
# 		print("\nEnter employee " + str(record + 1) + " details: ")
# 		for countOfField in range(len(empFields)):
# 			employeeData = input("\nEnter " + empFields[countOfField] + ": ")
# 			newData.append(employeeData)
# 	totalEmployeeData.extend(newData)

# def read():
# 	recordFound = 0
# 	for record in totalEmployeeData:
# 		# if record[0] == 'A':
# 			recordFound +=1
# 			print()
# 			for counter in range(len(empFields)):
# 				print(empFields[counter] + ": " + str(record[counter]))
# 			print()	
# 	if recordFound == 0:
# 			print("\nNo records found.\n")

# def exitProgram():
# 	File = open("jsonData.json", "w")
# 	convertToDict = {}
# 	# convertToDict = zip(empFields, totalEmployeeData)
# 	for index in range(len(empFields)):
# 		convertToDict[empFields[index]] = totalEmployeeData[index]
# 		print(convertToDict)
# 		File.write(str(convertToDict))
# 		File.close()
# 		exit(0)

# def readDataFromFile():
# 	global totalEmployeeData
# 	totalEmployeeData = []
# 	try: 
# 		File = open("jsonData.json", "r")
# 		totalEmployeeData = eval(File.read())
# 		File.close()
# 	except: 
# 		File = open("jsonData.json", "w")
# 		File.close()

# readDataFromFile()
# while True:
# 	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
# 	print("Please choose: \n1. New employee\n2. Show all employees\n3. Update an employee\n4. Delete an employee\n5. Search an employee\n6. exit\n")
# 	print("-------------------------------------------------------")
# 	choice = int(input("\nEnter your choice: "))
# 	if choice == 1:
# 		create()
# 	elif choice == 2:
# 		read()
# 	elif choice == 6:
# 		exitProgram()
# 	else:
# 		print("\nInvalid choice.")









#Python program to perform CRUD Operations with JSON file.

fieldsList = ["ID", "Name", "Age", "Salary"]

JSON_DATABASE = "jsonData.json"

def create():
	global dictionaryValues
	dictionaryValues = {}
	fieldsList.insert(0, "status")
	dictionaryValues[fieldsList[0]] = "active"
	for index in range(1, len(fieldsList)):
		dictionaryValues[fieldsList[index]] = input("\nEnter " + fieldsList[index] + ": ")
		dictionaryCopy = dictionaryValues.copy()		
	database["data"].append(dictionaryCopy)
	saveDataIntoFile()
	select = input("\nDo you want to continue? [y/n] ")
	if (select.upper() == 'Y'):
		create()

def display():
	recordFound = 0
	for record in database['data']:
		if record['status'] == "active":
			recordFound += 1
			print("\nEmployee record " + str(recordFound) + ": \n")

			for index in range(len(fieldsList)):
					print(fieldsList[index] + ": " + record[fieldsList[index]])
				# select = int(input("\nEnter your choice: "))
				# record[fieldsList[select]] = input("\nUpdate " + fieldsList[select] + ": ")

			# for key, value in record.items():
			# 	print(key + ": " + value)
	if recordFound == 0:
		print("\nNo records found.\n")

def search():
	recordFound = 0
	searchId = input("\nEnter " + fieldsList[0] + " to search: ")
	for record in database['data']:
		if record['status'] == "active":
			if searchId == record[fieldsList[0]]:
				recordFound += 1
				for index in range(len(fieldsList)):
					print(fieldsList[index] + ": " + record[fieldsList[index]])
				# for key, value in record.items():
				# 	print(key + ": " + value)
	if recordFound == 0:
		print("\nNo records found.\n")

def update():
	searchId = input("\nEnter " + fieldsList[0] + " to update: ")
	for record in database['data']:
		if record['status'] == "active":
			if searchId == record[fieldsList[0]]:
				print()
				for index in range(1, len(fieldsList)):
					print(str(index) + ". update" + fieldsList[index])
				select = int(input("\nEnter your choice: "))
				record[fieldsList[select]] = input("\nUpdate " + fieldsList[select] + ": ")
	saveDataIntoFile()

def delete():
	searchId = input("\nEnter " + fieldsList[0] + " to delete: ")
	for record in database['data']:
		if record['status'] == "active":
			if searchId == record[fieldsList[0]]:
				record['status'] = "inactive"
	saveDataIntoFile()
	


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

while True:
	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
	print("Please choose: \n1. New employee\n2. Show all employees\n3. search.\n4. Update.\n5. delete.\n6. exit\n")
	print("-" * 55)
	[create, display, search, update, delete, exit][int(input("\nEnter your choice: ")) - 1]()
	
































# for index in range(len(fieldKeys)):
# # 			fieldValues = input("\nEnter " + str(fieldKeys[index]) + ": ")
# # 			jsonFormat = dict(zip(fieldKeys, fieldValues))








# empFields = ["Employee ID", "Employee Name", "Employee Salary", "Employee Age", "Employee Address", "Employee Joining Date", "Employee Mobile Number"]

# def create():
# 	noOfRecords = int(input("\nHow many employee records do you want? "))
# 	for record in range(noOfRecords):
# 		newData = []
# 		status = 'A'
# 		newData.append(status)
# 		print("\nEnter employee " + str(record + 1) + " details: ")
# 		for countOfField in range(len(empFields)):
# 			employeeData = input("\nEnter " + empFields[countOfField] + ": ")
# 			newData.append(employeeData)
# 		totalEmployeeData.append(newData)

# def display():
# 	recordFound = 0
# 	for record in totalEmployeeData:
# 		if record[0] == 'A':
# 			recordFound +=1
# 			print()
# 			for counter in range(len(empFields)):
# 				print(empFields[counter] + ": " + str(record[counter + 1]))
# 			print()	
# 	if recordFound == 0:
# 			print("\nNo records found.\n")





# def readDataFromFile():
# 	global totalEmployeeData
# 	totalEmployeeData = []
# 	try: 
# 		File = open("jsonDatabase.json", "r")
# 		# totalEmployeeData = eval(Fisle.read())
# 		json.dump(totalEmployeeData)
# 		print(type(totalEmployeeData))
# 		File.close()
# 	except: 
# 		File = open("jsonDatabase.json", "w")
# 		File.close()

# readDataFromFile()

# def exitProgram():
# 	File = open("jsonDatabase.json", "w")
# 	File.write(eval(totalEmployeeData))
# 	File.close()
# 	exit(0)


# while True:
# 	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
# 	print("Please choose: \n1. New employee\n2. Show all employees\n3. Exit")
# 	print("-------------------------------------------------------")
# 	choice = int(input("\nEnter your choice: "))
# 	if choice == 1:
# 		create()
# 	elif choice == 2:
# 		display()
# 	elif choice == 3:
# 		exitProgram()
# 	else:
# 		print("\nInvalid choice.\n")


# import json
# fieldKeys = ["ID", "Name", "Age"]
# fieldValues = []
# # newValues = {}
# noOfRecords = int(input("\nHow many records do you want to create? "))
# for count in range(noOfRecords):
# 	print("\nEnter record " + str(count+1) + ": ")
# 	for index in range(len(fieldKeys)):
# 			fieldValues = input("\nEnter " + str(fieldKeys[index]) + ": ")
# 			jsonFormat = dict(zip(fieldKeys, fieldValues))
# 			# fieldValues.update({fieldKeys[index]:empData})
# File = open("crudJson.json", "a")
# File.write(str(jsonFormat))
# print(jsonFormat)


# print(jsonFormat)
# for (key, value) in fieldValues.items():
	# print(key, " :: " , value)
# 			print(fieldValues)
# newValues.update(fieldValues)
# print(newValues)
# # for i in range(noOfRecords):
# # print(fieldValues)

	



			# empData_json = json.loads(empData)
			# with open("sample.json", "w") as outfile:
			# 		json.dump(empData_json, outfile)
	# print(empData_json[0])



# with open("sample.json", "w") as outfile:
# 	json.dump(dictionary, outfile)

# dictionary = {
# 	"id" : 1,
# 	"name" : "rusheel",
# 	"age" : 22	
# }
# newData = {}
# print(type(newData))






# fieldKeys = ["ID", "Name", "Age"]
# fieldValues = ["1", "rusheel", "22"]
# newValues = {}
# # noOfRecords = int(input("\nHow many records do you want to create? "))
# # for count in range(noOfRecords):
# 	# print("\nEnter record " + str(count+1) + ": ")
# for index in range(len(fieldKeys)):
# 	# fieldValues = input("\nEnter " + str(fieldKeys[index]) + ": ")
# 	newValues[fieldKeys[index ]] = fieldValues[index]
# print(newValues)
# 			jsonFormat = dict(zip(fieldKeys, fieldValues))
# 			# fieldValues.update({fieldKeys[index]:empData})
# File = open("crudJson.json", "a")
# File.write(str(jsonFormat))
# print(jsonFormat)



# empFields = ["Employee ID", "Employee Name", "Employee Salary"]
# dictionaryValues = {}
# # mydict = {}
# database = {'data': []}
# def create():
# 	noOfRecords = int(input("\nhow many records do you want? "))
# 	for record in range(noOfRecords):
# 		for index in range(len(empFields)):
# 			dictionaryValues[empFields[index]] = input("\nEnter " + empFields[index] + ": ")
# 	# print(dictionaryValues)
# 	dictionaryCopy = dictionaryValues.copy()		
# 	# print(dictionaryCopy)
# 	database["data"].append(dictionaryCopy)
# 	print(database)
# 	# File.write(database)


# 	# dictionaryValues.clear()
# 	# print(dictionaryValues)
# 	# noOfRecords = int(input("\nHow many records do you want? "))
# 	# for record in range(noOfRecords):
# 	# 	for index in range(len(empFields)):
# 	# 		dictionaryValues[empFields[index]] = input("\nEnter " + empFields[index] + ": ")
# 	# # mydict = dictionaryValues.copy() 
# 	# print(dictionaryValues)
# 	# ListData = []
# 	# print("database data" ,str(database['data']))
# 	# ListData = database['data']
# 	# print("database stored in ListData: " + str(ListData))
# 	# ListData.append(dictionaryValues)
# 	# print(ListData)

# 	# database['data'] = ListData.copy()
# 	# print(str(database))


# def display():
# 	recordFound = 0
# 	for record in database['data']:
# 		recordFound += 1
# 		print("\nEmployee record " + str(recordFound) + ": \n")
# 		for key, value in record.items():
# 			print(key + ": " + value)
# 	# recordFound = 0
# 	# for x,y in dictionaryValues.items():
# 	# 	recordFound += 1
# 	# 	print(x,y)
# 	if recordFound == 0:
# 			print("\nNo records found.\n")

# def exitProgram():
# 	File = open("jsonData.json", "w")
# 	File.write(str(database))
# 	File.close()
# 	exit(0)

# def readDataFromFile():
# 	global database
# 	database = {'data': []}
# 	try: 
# 		# dictionaryValues = {}
# 		File = open("jsonData.json", "r")
# 		database = eval(File.read())
# 		File.close()
# 	except: 
# 		File = open("jsonData.json", "w")
# 		# File.write(str(database))
# 		File.close()
# 		readDataFromFile()


# readDataFromFile()

# while True:
# 	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
# 	print("Please choose: \n1. New employee\n2. Show all employees\n3. Update an employee\n4. Delete an employee\n5. Search an employee\n6. exit\n")
# 	print("-------------------------------------------------------")
# 	choice = int(input("\nEnter your choice: "))
# 	if choice == 1:
# 		create()
# 	elif choice == 2:
# 		display()
# 	elif choice == 6:
# 		exitProgram()
# 	else:
# 		print("\nInvalid choice.")
