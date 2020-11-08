# import xml.etree.ElementTree as xml


# # empFields = ["Employee ID", "Employee Name", "Employee Salary", "Employee Age", "Employee Address", "Employee Joining Date", "Employee Mobile Number"]
# # records = []
# def createXml():
# 	noOfRecords = input("\nHow many records do you want to create: ")

# 	root = xml.Element("employees")
# 	# id = 0
# 	employeeList = 0
# 	for record in range(int(noOfRecords)): 
# 		# id += 1
# 		# print(type(id))
# 		employeeList = xml.Element("employee")
# 		# employee1.set('id', str(id))
		
# 		idno = xml.SubElement(employeeList, "id")
# 		idno.text = input("\nEnter id: ")
# 		name = xml.SubElement(employeeList, "name")
# 		name.text = input("\nEnter name: ")
# 		age = xml.SubElement(employeeList, "age")
# 		age.text = input("\nEnter age: ")
# 		address = xml.SubElement(employeeList, "address")
# 		address.text = input("\nEnter address: ")
# 		joiningData = xml.SubElement(employeeList, "joiningData")
# 		joiningData.text = input("\nEnter joining date: ")
# 		salary = xml.SubElement(employeeList, "salary")
# 		salary.text = input("\nEnter salary: ")
# 		mobileNumber = xml.SubElement(employeeList, "mobileNumber")
# 		mobileNumber.text = input("\nEnter mobile number: ")

# 	root.append(employeeList)
# 	tree = xml.ElementTree(root)

# 	with open("employeexmldata2.xml", "wb") as files:
# 		tree.write(files)
# 		print(tree)
# 		files.close()



# def readXml():
# 	tree = xml.parse("employeexmldata2.xml")
# 	root = tree.getroot()

# 	tag = root.tag
# 	# print("Root tag name: ", tag)
# 	attr = root.attrib
# 	# print(attr)
# 	noOfEmployees = 0
# 	# for elem in root:
# 	# 	for subele in elem:
# 	# 		print(empFields[subele] + ": " + subele.text)
# 	for c in root.findall("employee"):
# 		noOfEmployees += 1
# 		# print(c)
# 		# print(att)
# 		print("\nEmployee " + str(noOfEmployees) + " is: ")
# 		# att = c.attrib
# 		# t = att.get('id')
# 		id = c.find('id').text
# 		print("ID: ", id)
# 		# print("ID: ", t)
# 		name = c.find('name').text
# 		print("Name: ", name)
# 		age = c.find('age').text
# 		print("Age: ", age)
# 		address = c.find('address').text
# 		print("Address: ", address)
# 		joiningData = c.find('joiningData').text
# 		print("Joining Date: ", joiningData)
# 		salary = c.find('salary').text
# 		print("Salary: ", salary)
# 		mobileNumber = c.find('mobileNumber').text
# 		print("Mobile NUmber: ", mobileNumber)





# while True:
# 	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
# 	print("Please choose: \n1. New employee\n2. Show all employees\n3. Update an employee\n4. Delete an employee\n5. Search an employee\n6. exit\n")
# 	print("-------------------------------------------------------")
# 	choice = int(input("\nEnter your choice: "))
# 	if choice == 1:
# 		createXml()
# 	elif choice == 2:
# 		readXml()






#Python program to perform create and read a Xml file.

import xml.etree.ElementTree as xml

fieldsList = ["ID", "Name", "Age"]
recordFound = 0
def create():
	noOfRecords = int(input("\nHow many records do you want to create? "))
	for count in range(noOfRecords):
		record = xml.Element("Employee")
		root.append(record)
		print("\nEnter record " + str(count+1) + ": ")
		for index in range(len(fieldsList)):
			field = xml.Element(fieldsList[index])
			field.text = input("Enter " + str(fieldsList[index]) + ": ")
			record.append(field)
	tree = xml.ElementTree(root)
	tree.write("database.xml")


def display():
	recordFound = 0
	for record in root:
		recordFound += 1
		for index in range(len(record)):
			print(record[index].tag + ": " + record[index].text)
		print()
	if recordFound == 0:
		print("\nNo records found.\n")


def readDataFromFile():
	try:
		global root
		tree = xml.parse("database.xml")
		root = tree.getroot()
	except : 
		file_object = open("database.xml", 'w')
		root = xml.Element('DataBase')
		tree = xml.ElementTree(root)
		tree.write("database.xml")
		file_object.close()

readDataFromFile()


while True:
	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
	print("Please choose: \n1. New employee\n2. Show all employees\n3. Exit")
	print("-------------------------------------------------------")
	choice = int(input("\nEnter your choice: "))
	if choice == 1:
		create()
	elif choice == 2:
		display()
	elif choice == 3:
		exit(0)
	else:
		print("\nInvalid choice.\n")












































#Python program to create and read a XML file.

import xml.etree.ElementTree as XML

DATABASE_FILE = "xmlDatabaseFile.XML"

fieldsList = ["ID", "Name", "Age", "Salary"]
recordFound = 0

def create():
	status = "Active"
	fieldsList[0] = status
	# print(fieldsList)
	record = XML.SubElement(root ,"Employee")
	for index in range(len(fieldsList)):
		field = XML.Element(fieldsList[index])
		field.text = input("\nEnter " + str(fieldsList[index]) + ": ")
		record.append(field)
	tree = XML.ElementTree(root)
	tree.write(DATABASE_FILE)
	select = input("\nDo you want to continue? [y/n] ")
	if (select.upper() == 'Y'):
		create()


def display():
	recordFound = 0
	for record in root:
		recordFound += 1
		print("\nEmployee record " + str(recordFound) + ": \n")
		for index in range(len(record)):
			print(record[index].tag + ": " + record[index].text)
		print()
	if recordFound == 0:
		print("\nNo records found.\n")


def search():
	recordFound = 0
	searchID = input("\nEnter employee ID to search: ") 
	print()
	for record in root:
		for index in range(len(record)):
			if searchID == record[0].text:
				recordFound += 1
				print(record[index].tag + ": " + record[index].text)
	if recordFound == 0:
		print("Invalid ID.\n")

def update():
	recordFound = 0
	searchID = input("\nEnter employee ID to update: ")
	for record in root:
		if searchID == record[0].text:
			print()
			for index in range(1, len(record)):
				print(str(index) + ". update " + record[index].tag)
			select = int(input("\nEnter your choice: "))
			record[select].text = input("\nUpdate " + record[select].tag + ": ")
	tree = XML.ElementTree(root)
	tree.write(DATABASE_FILE)

def delete():
	pass

def saveDataFromFile():
	try:
		global root
		tree = XML.parse(DATABASE_FILE)
		root = tree.getroot()
	except : 
		file_object = open(DATABASE_FILE, 'w')
		root = XML.Element('DataBase')
		tree = XML.ElementTree(root)
		tree.write(DATABASE_FILE)
		file_object.close()

saveDataFromFile()


while True:
	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
	print("Please choose: \n1. New employee\n2. Show all employees\n3. Search.\n4. Update.\n5. Exit")
	print("-" * 55)
	[create, display, search, update, exit][int(input("\nEnter your choice: "))-1]()
	


	