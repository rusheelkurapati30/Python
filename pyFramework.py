#Python framework program.

DATABASE_FILE = 'databaseFile.dat'

fields = []
fieldsFile = open("fields.cfg", "r") 
fields = fieldsFile.readlines()
fieldsFile.close()

def create():
	noOfRecords = int(input("\nHow many records do you want? "))
	for record in range(noOfRecords):
		newDate = []
		status = 'A'
		newDate.append(status)
		print("\nEnter record " + str(record + 1) + " details: ")
		for countOffield in range(len(fields)):
			fieldsValue = input("\nEnter " + fields[countOffield][:-1] + ": ")
			newDate.append(fieldsValue)
		totalRecordData.append(newDate)
		# print(totalRecordData)

def display():
	recordFound = 0
	for record in totalRecordData:
		if record[0] == 'A':
			recordFound +=1
			print()
			for counter in range(len(fields)):
				print(fields[counter][:-1] + ": " + str(record[counter + 1]))
			print()	
	if recordFound == 0:
			print("\nNo records found.\n")

def search():
	searchId = input("\nEnter " + fields[0][:-1] + " to search: ")
	recordFound = 0
	for record in totalRecordData:
		if record[0] == 'A' and record[1] == searchId:
			recordFound += 1
			# print("record found.")
			print()
			for counter in range(len(fields)):
				print(fields[counter][:-1] + ": " + str(record[counter + 1]))
	if recordFound == 0:
		print("\nInvalid ID.\n")

def update():
	counter = 0
	recordFound = 0
	updated = 0
	searchId = input("\nEnter " + fields[0][:-1] + " to update: ")
	for record in totalRecordData:
		if record[0] == 'A' and record[1] == searchId:
			recordFound += 1
			# print("record found.")
			print("\nPlease choose any field to update: \n")
			for countOffield in range(len(fields) - 1):
				print("%d . To update %s" % (countOffield + 1, fields[countOffield + 1]))
			choice = int(input("\nEnter your choice: "))
			if choice > 0 and choice < len(fields):
				totalRecordData[counter][choice+1] = input("\nEnter " + fields[choice][:-1] + " to update: ")
				updated += 1
			else:
				print("\nInvalid ID.")
		counter += 1
	if updated >= 1:
		print("\nUpdated successfully.\n")
	if recordFound == 0:
		print("\nInvalid ID.\n") 

def delete():
	counter = -1
	searchId = input("\nEnter " + fields[0][:-1] + " to delete: ")
	recordFound = 0
	for record in totalRecordData:
		# print(totalRecordData)
		counter += 1
		if record[0] == 'A' and record[1] == searchId:
			recordFound += 1
			# print("record found.")
			totalRecordData[counter][0] = 'I'
	if recordFound == 0:
		print("\nInvalid ID.\n")
	else:
		print("\nRecord deleted.\n")

def saveDataIntoFile():
	File = open(DATABASE_FILE, "w")
	File.write(str(totalRecordData))
	File.close()
	exit(0)

def loadDataFromFile():
	global totalRecordData
	totalRecordData = []
	try: 
		File = open(DATABASE_FILE, "r")
		totalRecordData = eval(File.read())
		File.close()
	except: 
		File = open(DATABASE_FILE, "w")
		File.close()

loadDataFromFile()

def showMenu():
	while True:
		menuFile = open("menu.cfg", "r")
		menuLines = menuFile.readlines()
		print()
		for line in menuLines:
			print(line, end = "")
		choice = int(input("\nEnter your choice: "))
		if choice == 1:
			create()
		elif choice == 2:
			display()
		elif choice == 3:
			update()
		elif choice == 4:
			search()
		elif choice == 5:
			delete()
		elif choice == 6:
			saveDataIntoFile()
		else:
			print("\nInvalid choice.\n")
		menuFile.close()

showMenu()

