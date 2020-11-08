File = open("databaseFile.dat", "a")
names = input("Enter Name: ")
File.write(names + "\n")
names = input("Enter Age: ")
File.write(names + "\n")
# print(names, end="")
File.close()



# # Python program to perform crud operations
# empFields = ["employeeId", "employeeName", "employeeSalary"]
# totalEmployeeData = []
# recordFound = 0
# # dataFromFile = ""
# # totalEmployeeData = [['A', 1, "rusheel", 1500],['A', 2, "ravi", 2000],['A', 3, "raju", 2500]]
# # status = 'A'

# def create():
	
# 	# File = open("datbaseFile.dat", "a")
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
# 	print(totalEmployeeData)

# def read():
# 	recordFound = 0
# 	# File = open("databaseFile.dat", "r")
# 	# totalEmployeeData = File.readlines()
# 	# print(totalEmployeeData)
# 	for record in totalEmployeeData:
# 		if record[0] == 'A':
# 			recordFound +=1
# 			for counter in range(len(empFields)):
# 				print(empFields[counter] + ": " + str(record[counter + 1]))
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
# 	recordFound = 0
# 	searchId = input("Enter ID to update: ")
# 	for record in totalEmployeeData:
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
# 	recordFound = 0
# 	# print("hi")
# 	for record in totalEmployeeData:
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
# 	recordFound = 0
# 	for record in totalEmployeeData:
# 		if record[0] == 'A' and record[1] == searchId:
# 			recordFound += 1
# 			print("record found.")
# 			for counter in range(len(empFields)):
# 				print(empFields[counter] + ": " + str(record[counter + 1]))
# 	if recordFound == 0:
# 		print("\nInvalid ID.\n")

# def exitProgram():
# 	File = open("databaseFile.dat", "w")
# 	File.write(str(totalEmployeeData))
# 	print("Data saved to file: " + str(totalEmployeeData))
# 	exit(0)

# def readDataFromFile():
# 	# dataFromFile
# 	try: 
# 		File = open("databaseFile.dat", "r+")
# 		totalEmployeeData = File.readlines()
# 		# dataFromFile = []
# 		# dataFromFile.append(File.read())
# 		# print(dataFromFile)
# 		# print(dataFromFile[0])
# 		# totalEmployeeData = dataFromFile.copy()
# 		print(str(totalEmployeeData))
# 		File.close()
# 	except: 
# 		File = open("databaseFile.dat", "w")
# 		File.close()

# readDataFromFile()
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
# 	elif choice == 6:
# 		exitProgram()
# 	else:
# 		print("\nInvalid choice.")
