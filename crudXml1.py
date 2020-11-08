#Python program to perform create and read a Xml file.

import xml.etree.ElementTree as xml
DATABASE_FILE = "xmldatabase.xml"

fieldsList = ["Employee ID", "Employee Name", "Employee Age"]
recordFound = 0
def create():
	record = xml.SubElement(root ,"Employee")
	for index in range(len(fieldsList)):
		field = xml.Element(fieldsList[index])
		field.text = input("\nEnter " + str(fieldsList[index]) + ": ")
		record.append(field)
	tree = xml.ElementTree(root)
	tree.write(DATABASE_FILE)
	select = input("\nDo you want to continue? [y/n]")
	if (select == 'y') or (select == 'Y'):
		create()


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
		tree = xml.parse(DATABASE_FILE)
		root = tree.getroot()
	except : 
		file_object = open(DATABASE_FILE, 'w')
		root = xml.Element('DataBase')
		tree = xml.ElementTree(root)
		tree.write(DATABASE_FILE)
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
