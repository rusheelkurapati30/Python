
#Python program to perform create and read a csv file.

import csv

CSV_DATABASE_FILE = "mycsv1.csv"

totalData = []

def create():
	with open(CSV_DATABASE_FILE, 'a', newline = '') as f:
		global totalRecords
		noOfRecords = int(input("\nHow many records do you want? "))
		for record in range(noOfRecords):
			listData = []
			print("\nEnter record " + str(record+1) + ": ")
			for index in range(len(totalData[0])):
				listData.append(input("\nEnter " +  totalData[0][index] + ": "))
			totalData.append(listData) 
			thewriter = csv.writer(f)
			thewriter.writerow(listData)

def display():
	# with open('CSV_DATABASE_FILE') as f:
	# 	reader = csv.reader(f)
	recordFound = 0
	for counter in range(1, len(totalData)):
		recordFound += 1
		for index in range(len(totalData[counter])):
			print(totalData[0][index] + ": " + totalData[counter][index])
		print()
	if recordFound == 0:
		print("\nNo records found.\n")


def saveDataIntoFile():
	with open(CSV_DATABASE_FILE, 'w', newline = '') as f:
		thewriter = csv.writer(f)
		for row in totalData:
			thewriter.writerow(row)
	exit(0)

def loadDataFromCsvIntoList():
	with open(CSV_DATABASE_FILE) as f:
		reader = csv.reader(f)
		for row in reader:
			totalData.append(row)


loadDataFromCsvIntoList()

def saveHeaders():
	with open(CSV_DATABASE_FILE, 'w', newline = '') as f:
		thewriter=csv.writer(f)
		thewriter.writerow(['Id','Name','Age','Salary'])

saveHeaders()

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
		saveDataIntoFile()
		# exit(0)
	else:
		print("\nInvalid choice.\n")
