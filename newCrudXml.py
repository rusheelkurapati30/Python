#Python program to perform CRUD Operations with XML file.

import xml.etree.ElementTree as XML
import requests
import random
import os


DATABASE_FILE = "xmlDatabaseFile.XML"

fieldsList = ["ID", "Name", "Age", "Salary"]


def create():
	record = XML.SubElement(root ,"Employee")
	statusField = XML.SubElement(record, "Status")
	statusField.text = 'active'
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
		if record[0].text == "active":
			recordFound += 1
			print("\nEmployee record " + str(recordFound) + ": \n")
			for index in range(1, len(record)):
				print(record[index].tag + ": " + record[index].text)
			print()
	if recordFound == 0:
		print("\nNo records found.\n")


def search():
	modify('search')


def update():
	modify('update')


def delete():
	modify('delete')

def modify(mode):
	recordFound = 0
	searchID = input("\nEnter " + fieldsList[0] + " to " + mode + ": ")
	for record in root:
		if (record[0].text == "active") and (searchID == record[1].text):
			recordFound += 1
			if mode == 'update':
				print()
				for index in range(2, len(record)):
					print(str(index-1) + ". update " + record[index].tag)
				select = int(input("\nEnter your choice: "))
				record[select+1].text = input("\nUpdate " + record[select+1].tag + ": ")
				tree = XML.ElementTree(root)
				tree.write(DATABASE_FILE)
				print("\nRecord updated.\n")
			elif mode == 'delete':
				record[0].text = "inactive"
				tree = XML.ElementTree(root)
				tree.write(DATABASE_FILE)
				print("\nRecord deleted.\n")
			else:
				print()
				for index in range(1, len(record)):
					print(record[index].tag + ": " + record[index].text)

	if recordFound == 0:
		print("\nInvalid ID.\n")
	
def verifyOtp():
	otp = ''
	for counter in range(6):
		otp += str(random.randint(0, 9))
	
	message = "Your OTP is " + otp + "."
	mobileNumber = int(input("\nEnter your mobile number to receive OTP: "))
	
	url = "http://psms.goforsms.com/API/sms.php?username=srushtiimages&password=tecnics&from=WEBSMS&to=%d&msg=%s&type=1&dnd_check=0" % (mobileNumber, message)
	response = requests.get(url)
	
	otpVerification = input("\nPlease enter OTP to login: ")

	if otpVerification == otp:
		print("\nlogin successful.") 
	else:
		print("\nThe OTP entered is incorrect.")
		exit(0)

verifyOtp()

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






def showMenu():
	while True:
		print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
		print("Please choose: \n1. New employee\n2. Show all employees\n3. Search.\n4. Update.\n5. Delete.\n6. Exit")
		print("-" * 55)
		[create, display, search, update, delete, exit][int(input("\nEnter your choice: "))-1]()
	

showMenu()

	