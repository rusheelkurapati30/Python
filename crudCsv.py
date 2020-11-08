# import csv
# totalRecords = 0
# fieldsList = ["Employee ID", "Employee name", "Employee age"]
# idno = []
# name = []
# age = []


# def create():
# 	# header = 0
# 	global totalRecords
# 	noOfRecords = int(input("\nHow many records do you want? "))
# 	# totalRecords += noOfRecords
# 	# print(totalRecords)
# 	with open('mycsv.csv', 'a', newline = '') as f:
# 		for record in range(noOfRecords):
# 			idno = input("\nEnter ID: ")
# 			name = input("\nEnter Name: ")
# 			age = input("\nEnter Age: ")
			
# 			thewriter = csv.writer(f)
# 			thewriter.writerow([idno,name,age])

# def display():
# 	# data = []
# 	try: 
# 		with open('mycsv.csv') as f:
# 			reader = csv.reader(f)
# 			for row in reader:
# 				# print(len(row))
# 				idno.append(row[0])
# 				name.append(row[1])
# 				age.append(row[2])
# 			# print("id : " + str(idno))
# 			# print("names : " + str(name))
# 			# print("ages : " + str(age))
# 			for index in range(len(idno)):
# 				counter = 0
# 				recordFound +=1
# 				# for lists in range(len(fieldsList)):
# 				# print(len(fieldsList))
# 				print(fieldsList[counter] + ": " +idno[index])
# 				counter += 1
# 				print(fieldsList[counter] + ": " +name[index])
# 				counter += 1
# 				print(fieldsList[counter] + ": " +age[index])
# 				print()
# 	except:
# 		print("\nNo records found.\n")

			# vals = row.split(',')
			# print(row[0], row[1], row[2])
		# print(vals[1])
		# line = f.readline()
		# print(line)
		# firstItem = line.split(',')
		# print(firstItem[0])
	# 	# lineCount = 0
	# 	for row in reader:
	# 		for (i,v) in enumerate(row):
	# 			columns[i].append(v)
	# print(columns[0])
			# print(row[0] +","+ row[1] +","+ row[2])
		# for row in reader:
		# 	print(f'column names are {", ".join(row)}')
		# 	lineCount += 1
		# else:
		# 	print(f'\t{row[0]} name is {row[1]} and age is {row[2]}.')
		# 	lineCount += 1
		# print(f'processed {lineCount} lines.')

		# for row in csv.DictReader(f):
		# 	for key, value in row.items():
		# 		data[key].append(value)


		# reader = csv.reader(f, delimiter = "\t")
		# for row in reader:
		# 	print(row)

		# for i, line in enumerate(reader):
		# 	print("line[{}] = {}".format(i, line))


		# lis = [line.split() for line in f]
		# for i, x in enumerate(lis):
		# 	print("line{0} = {1}".format(i,x))
		# 	print(x[0])


		# for i, line in enumerate(f):
		# 	print("line {0} = {1}".format(i, split('')))


		# thereader = csv.reader(f)
		# for row in thereader:
		# 	print(row[0])


		# 	data.append(row)
		# for items in data:
		# 	print(items[0] + items[1])



	# counter = -1
	# with open('mycsv.csv') as f:
		# print(thereader)
		# for column in thereader:
		# 	print(column)
		# 	for row in column:
		# 		counter += 1
		# 		# print(row + ": " + column[row])
		# 		print(fieldsList[counter]  + " : " + row )
		# 	counter = -1
		# 	for row in column:
		# 		counter += 1
		# 		print(fieldsList[counter]  + " : " + column[row] )
		# 	counter = -1
		# 	for row in column:
		# 		counter += 1
		# 		print(fieldsList[counter]  + " : " + column[row] )



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
# 		exit(0)
# 	else:
# 		print("\nInvalid choice.\n")

























# from csv import writer
# with open("csvFile.csv", "w") as f:
# 	csvWriter = writer(f)
# 	# csvWriter.writerow(["name", "country"])
# 	# csvWriter.writerow(["Rusheel", "India"])
# 	# csvWriter.writerow(["Sam", "UK"])

# 	csvWriter.writerows([["name", "country"], ["Rusheel", "India"], ["Raju", "India"]])





















# from csv import DictWriter, DictReader
# 	# csvWriter.writerow({
# 	# 	'name':'Rusheel',
# 	# 	'address':'hanuman nagar',
# 	# 	'age':'22'
# 	# 	})
# 	# csvWriter.writerow({
# 	# 	'name':'Suresh',
# 	# 	'address':'ecil',
# 	# 	'age':'23'
# 	# 	})

# def create(): 
# 	with open("csvFile1.csv", "w") as f:
# 		csvWriter = DictWriter(f, fieldnames = ['name', 'address', 'age'])
# 		# next(csvWriter)
# 		csvWriter.writeheader()
# 		noOfRecords = int(input('How many records do you want? '))
# 		for record in range(noOfRecords):
# 			inputName = input('Enter name: ')
# 			inputAddress = input('Enter address: ')
# 			inputAge = input('Enter age: ')
# 			csvWriter.writerows([
# 				{'name':inputName,
# 				'address':inputAddress,
# 				'age':inputAge}
# 				])

# def display():
# 	with open("csvFile1.csv", "r") as r:
# 		csvReader = DictReader(r)

# 		for line in csvReader:
# 			print(line)

# while True:
# 	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
# 	print("Please choose: \n1. New employee\n2. Show all employees\n3. Update an employee\n4. Delete an employee\n5. Search an employee\n6. exit\n")
# 	print("-------------------------------------------------------")
# 	choice = int(input("\nEnter your choice: "))
# 	if choice == 1:
# 		create()
# 	elif choice == 2:
# 		display()


# import csv

# with open('employee_file.csv', mode='a') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     # employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     # employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
#     noOfRecords = int(input('How many records do you want? '))
#     for record in range(noOfRecords):
#     	inputName = input("Enter name: ")
#     	inputAddress = input("Enter address")
#     	inputAge = input("Enter age: ")
#     	employee_writer.writerows([
#     		[inputName,
#     		inputAddress,
#     		inputAge]
#     		])

	# for record in range(noOfRecords):
	# 	inputName = input('Enter name: ')
	# 	inputAddress = input('Enter address: ')
	# 	inputAge = input('Enter age: ')
	# 	csvWriter.writerows([
	# 		{'name':inputName,
	# 		'address':inputAddress,
	# 		'age':inputAge}
	# 		])







# import csv

# empFields = ["name", "address", "age"]

# def create(): 
# 	with open('employeeFile.csv', mode='a') as employeeFile:
# 	    employeeData = csv.writer(employeeFile)
# 	    # employeeData = csv.writer(employeeFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# 	    # employee_writer.writerow(['John Smith', 'Accounting', 'November'])
# 	    # employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
# 	noOfRecords = int(input("\nhow many records do you want? "))
# 	for record in range(noOfRecords):
# 		print("\nEnter employee record " + str(record+1) + ": ")
# 		for index in range(len(empFields)):
# 				# dictionaryValues[empFields[index]] = input("\nEnter " + empFields[index] + ": ")
# 		    	empFields[index] = input("\nEnter " + empFields[index] + ": ")
# 		    	# inputAddress = input("Enter address: ")
# 		    	# inputAge = input("Enter age: ")
# 		    	# employeeData.writerows([
# 		    	# 	[inputName,
# 		    	# 	inputAddress,
# 		    	# 	inputAge]
# 		    	# 	])

# 		    	employeeData.writerows([
# 		    		[empFields[index],]
# 		    		])
# def display():
# 	with open('employeeFile.csv') as csv_file:
# 	    csv_reader = csv.reader(csv_file, delimiter=',')
# 	    line_count = 0
# 	    for row in csv_reader:
# 	    	for fields in range(len(empFields) + 1):
# 	        # if line_count == 0:
# 	            print(empFields[fields] + ": " + str(row[fields]))
# 	            # line_count += 1
# 	            # print(f'Column names are {", ".join(row)}')
# 	            # line_count += 1
# 	        # else:
# 	            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
# 	            # line_count += 1
# 	    # print(f'Processed {line_count} lines.')

# while True:
# 	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
# 	print("Please choose: \n1. New employee\n2. Show all employees\n3. exit\n")
# 	print("-------------------------------------------------------")
# 	choice = int(input("\nEnter your choice: "))
# 	if choice == 1:
# 		create()
# 	elif choice == 2:
# 		display()
# 	elif choice == 3:
# 		exit(0)
# 	else:
# 		print("\nInvalid choice.\n")





	# 	record = xml.Element("Employees")
	# root.append(record)
	# noOfRecords = int(input("\nHow many records do tyou want to create? "))
	# for count in range(noOfRecords):
	# 	print("\nEnter record " + str(count+1) + ": ")
	# 	for index in range(len(fieldsList)):
	# 		field = xml.Element(fieldsList[index])
	# 		field.text = input("Enter " + str(fieldsList[index]) + ": ")
	# 		record.append(field)
	# 	tree = xml.ElementTree(root)
	# 	tree.write("database.xml")






















































# #Python program to perform create and read a csv file.

# import csv

# CSV_DATABASE_FILE = "mycsv1.csv"

# totalData = []

# def create():
# 	with open(CSV_DATABASE_FILE, 'a', newline = '') as f:
# 		global totalRecords
# 		noOfRecords = int(input("\nHow many records do you want? "))
# 		for record in range(noOfRecords):
# 			listData = []
# 			print("\nEnter record " + str(record+1) + ": ")
# 			for index in range(len(totalData[0])):
# 				listData.append(input("\nEnter " +  totalData[0][index] + ": "))
# 			totalData.append(listData) 
# 			thewriter = csv.writer(f)
# 			thewriter.writerow(listData)

# def display():
# 	# with open('CSV_DATABASE_FILE') as f:
# 	# 	reader = csv.reader(f)
# 	recordFound = 0
# 	for counter in range(1, len(totalData)):
# 		recordFound += 1
# 		for index in range(len(totalData[counter])):
# 			print(totalData[0][index] + ": " + totalData[counter][index])
# 		print()
# 	if recordFound == 0:
# 		print("\nNo records found.\n")


# def saveDataIntoFile():
# 	with open(CSV_DATABASE_FILE, 'w', newline = '') as f:
# 		thewriter = csv.writer(f)
# 		for row in totalData:
# 			thewriter.writerow(row)
# 	exit(0)

# def loadDataFromCsvIntoList():
# 	with open(CSV_DATABASE_FILE) as f:
# 		reader = csv.reader(f)
# 		for row in reader:
# 			totalData.append(row)


# loadDataFromCsvIntoList()

# # def saveHeaders():
# # 	with open('CSV_DATABASE_FILE', 'w', newline = '') as f:
# # 		writer.csv.writer(f)
# # 		writer.writerow(['Id','Name','Age','Salary'])

# # saveHeaders()

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
# 		saveDataIntoFile()
# 		# exit(0)
# 	else:
# 		print("\nInvalid choice.\n")










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
	with open('CSV_DATABASE_FILE', 'w', newline = '') as f:
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









