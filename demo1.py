import csv
totalData = []

def create():
	with open('mycsv.csv', 'a', newline = '') as f:
		global totalRecords
		noOfRecords = int(input("\nHow many records do you want? "))
		for record in range(noOfRecords):
			listData = []
			for index in range(len(totalData[0])):
				if index == (len(totalData[0])-1):
					listData.append(input("\nEnter " +  totalData[0][index][:-1] + ": "))
				else:
					listData.append(input("\nEnter " +  totalData[0][index] + ": "))
			totalData.append(listData) 
			print(listData)
			thewriter = csv.writer(f)
			thewriter.writerow(listData)

def display():
	# with open('mycsv.csv') as f:
	# 	reader = csv.reader(f)
	
		for counter in range(1, len(totalData)):
			for index in range(len(totalData[counter])):
				if index == (len(totalData[0])-1):
					print(totalData[0][index][:-1] + ": " + totalData[counter][index])
				else:
					print(totalData[0][index] + ": " + totalData[counter][index])

			print()
	except:
		print("\nNo records found.\n")


def saveDataIntoFile():
	print(totalData)
	with open('mycsv.csv', 'w', newline = '') as f:
		thewriter = csv.writer(f)
		for row in totalData:
			thewriter.writerow(row)
			print(row)
			# exit(0)

def loadDataFromCsvIntoList():
	# global totalData
	with open('mycsv.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			totalData.append(row)
	print(totalData)
	# if (totalData[0][len(totalData[0])-1][-1]) != '\n':
	# 	totalData[0][len(totalData[0])-1] = totalData[0][len(totalData[0])-1] + '\n'
	# 	print(totalData[0])


loadDataFromCsvIntoList()

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
		exit(0)
	else:
		print("\nInvalid choice.\n")