#Python program to perform crud operations

empFields = ["Employee ID", "Employee Name", "Employee Salary", "Employee Age", "Employee Address", "Employee Joining Date", "Employee Mobile Number"]
recordFound = 0
def create():
	noOfRecords = int(input("\nHow many employee records do you want? "))
	for record in range(noOfRecords):
		newData = []
		status = 'A'
		newData.append(status)
		print("\nEnter employee " + str(record + 1) + " details: ")
		for countOfField in range(len(empFields)):
			employeeData = input("\nEnter " + empFields[countOfField] + ": ")
			newData.append(employeeData)
		totalEmployeeData.append(newData)

def read():
	recordFound = 0
	for record in totalEmployeeData:
		if record[0] == 'A':
			recordFound +=1
			print()
			for counter in range(len(empFields)):
				print(empFields[counter] + ": " + str(record[counter + 1]))
			print()	
	if recordFound == 0:
			print("\nNo records found.\n")

def update():
	counter = 0
	recordFound = 0
	updated = 0
	searchId = input("Enter ID to update: ")
	for record in totalEmployeeData:
		if record[0] == 'A' and record[1] == searchId:
			recordFound += 1
			# print("record found.")
			print("\n1. To update name")
			print("2. To update salary")
			print("3. To update age")
			print("4. To update address")
			print("5. To update joining date")
			print("6. To update mobile number\n")
			choice = int(input("\nEnter your choice: "))
			if choice == 1:
				totalEmployeeData[counter][2] = input("\nEnter name to update: ")
				updated += 1
			if choice == 2:
				totalEmployeeData[counter][3] = input("\nEnter salary to update: ")
				updated += 1
			if choice == 3:
				totalEmployeeData[counter][4] = input("\nEnter age to update: ")
				updated += 1
			if choice == 4:
				totalEmployeeData[counter][5] = input("\nEnter address to update: ")
				updated += 1
			if choice == 5:
				totalEmployeeData[counter][6] = input("\nEnter Joining date to update: ")
				updated += 1
			if choice == 6:
				totalEmployeeData[counter][7] = input("\nEnter mobile number to update: ")
				updated += 1
		counter += 1
	if updated >= 1:
		print("\nUpdated successfully.\n")
	if recordFound == 0:
		print("\nInvalid ID.\n")
	
def delete():
	counter = -1
	searchId = input("Enter ID to delete: ")
	recordFound = 0
	# print("hi")
	for record in totalEmployeeData:
		# print(totalEmployeeData)
		counter += 1
		if record[0] == 'A' and record[1] == searchId:
			recordFound += 1
			# print("record found.")
			totalEmployeeData[counter][0] = 'I'
	if recordFound == 0:
		print("\nInvalid ID.\n")
	else:
		print("\nRecord deleted.\n")

def search():
	searchId = input("Enter ID to search: ")
	recordFound = 0
	for record in totalEmployeeData:
		if record[0] == 'A' and record[1] == searchId:
			recordFound += 1
			# print("record found.")
			for counter in range(len(empFields)):
				print(empFields[counter] + ": " + str(record[counter + 1]))
	if recordFound == 0:
		print("\nInvalid ID.\n")

def exitProgram():
	File = open("databaseFile1.dat", "w")
	File.write(str(totalEmployeeData))
	File.close()
	exit(0)

def readDataFromFile():
	global totalEmployeeData
	totalEmployeeData = []
	try: 
		File = open("databaseFile1.dat", "r")
		totalEmployeeData = eval(File.read())
		File.close()
	except: 
		File = open("databaseFile1.dat", "w")
		File.close()

readDataFromFile()
while True:
	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
	print("Please choose: \n1. New employee\n2. Show all employees\n3. Update an employee\n4. Delete an employee\n5. Search an employee\n6. exit\n")
	print("-------------------------------------------------------")
	choice = int(input("\nEnter your choice: "))
	if choice == 1:
		create()
	elif choice == 2:
		read()
	elif choice == 3:
		update()
	elif choice == 4:
		delete()
	elif choice == 5:
		search()
	elif choice == 6:
		exitProgram()
	else:
		print("\nInvalid choice.")


# while True:
# 	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
# 	print("Please choose: \n1. New employee\n2. Show all employees\n3. Search.\n4. Update.\n5. Exit")
# 	print("-" * 55)
# 	[create, display, search, update, exit][int(input("\nEnter your choice: "))-1]()
# 	