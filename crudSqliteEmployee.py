#Python program to perform CRUD operations using SQLite database.

import sqlite3


conn = sqlite3.connect('employees.sqlite')
cursor = conn.cursor()

def createTableIfNotExist():
	cursor.execute('''select count(name) from sqlite_master where type = 'table' and name = 'EMPLOYEE' ''')
	if cursor.fetchone()[0] != 1:
		query = ('''CREATE TABLE EMPLOYEE(STATUS TEXT NOT NULL
										ID INTEGER PRIMARY KEY NOT NULL,
 										NAME TEXT NOT NULL,
 										AGE INTEGER NOT NULL,
 										SALARY INTEGER NOT NULL
 										);''')
			

		cursor.execute(query)
		conn.commit()


createTableIfNotExist()


def insert():
	try:
		while True:
			ID = int(input("\nEnter ID: "))
			NAME = input("\nEnter Name: ")
			AGE = int(input("\nEnter Age: "))
			SALARY = int(input("\nEnter Salary: "))

			query = '''INSERT INTO EMPLOYEE(STATUS, ID, NAME, AGE, SALARY) VALUES ( ?,?,?,?,? )'''
			cursor.execute(query, (ID, NAME, AGE, SALARY))

			conn.commit()

			choice = input("\nDo you want to continue? [y/n] ")
			if (choice.upper() != 'Y'):
					break
	except:
		print("Insert Valid Data")


def showData():
	try: 
		query = '''SELECT ID, NAME, AGE, SALARY FROM EMPLOYEE;'''

		cursor.execute(query)
		employeeData = cursor.fetchall()

		if employeeData:
			print_data(employeeData)
			
		conn.commit()
	except:
		print("No records found.")


def print_data(employeeData):
	print('\nID\tNAME\t\tAGE\tSALARY\n')
	for employeeRecord in employeeData:
		print('{0}\t{1}\t\t{2}\t{3}'.format(employeeRecord[0], employeeRecord[1], employeeRecord[2], employeeRecord[3]))


def show_data_by_id(ID):
	global recordFound
	recordFound = 0
	query = '''SELECT ID, NAME, AGE, SALARY FROM EMPLOYEE WHERE ID = {}''' .format(ID)

	cursor.execute(query)
	employeeData = cursor.fetchall()

	conn.commit()

	if employeeData:
		recordFound += 1
		print_data(employeeData)		
	else:
		print("\nNo record found with ID: ", ID)


def update():
	ID = int(input('\nEnter Id: '))
	show_data_by_id(ID)
	if recordFound == 1:
		print("\n1. To update name")
		print("2. To update age")
		print("3. To update salary")

		choice = int(input("\nEnter your choice: "))
		if choice == 1:
			NAME = input("\nEnter name to update: ")
			query = '''UPDATE EMPLOYEE SET NAME = ? WHERE ID = ?'''
			cursor.execute(query,(NAME, ID))

		if choice == 2:
			AGE = input("\nEnter age to update: ")
			query = '''UPDATE EMPLOYEE SET AGE = ? WHERE ID = ?'''
			cursor.execute(query,(AGE, ID))

		if choice == 3:
			SALARY = input("\nEnter salary to update: ")
			query = '''UPDATE EMPLOYEE SET SALARY = ? WHERE ID = ?'''
			cursor.execute(query,(SALARY, ID))

		conn.commit()

		print("\nRecord updated")


def delete():
	ID = int(input('\nEnter Id: '))

	show_data_by_id(ID)

	if recordFound == 1:

		query = '''DELETE FROM EMPLOYEE WHERE ID = {}''' .format(ID)

		cursor.execute(query)
		employeeData = cursor.fetchall()

		conn.commit()

		print("\nRecord deleted")
	


def search():
	ID = int(input("\nEnter ID: "))
	show_data_by_id(ID)

def exitProgram():
	conn.close()
	exit(0)

def showMenu():
	while True:
		print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
		print("Please choose: \n1. Add New employee Record\n2. Show all employees\n3. Update an employee Record\n4. Delete an employee Record\n5. Search an employee Record\n6. exit\n")
		print("-" * 65)
		[insert, showData, update, delete, search, exitProgram][int(input("\nEnter your choice: "))-1]()	

showMenu()
	





















				



# import sqlite3
# conn = sqlite3.connect('employees.sqlite')

# cursor = conn.cursor()

# query = '''
#     SELECT ID, NAME, AGE, SALARY FROM EMPLOYEE;
# '''

# cursor.execute(query)
# employeeData = cursor.fetchall()

# for employeeRecord in query:
# 	print(employeeRecord)
# conn.commit()
# conn.close()



# import sqlite3

# def showData():
# 	employees = read()
# 		# print("table doesnt exist")
# 	print('\nID\tNAME\t\tAGE\tSALARY\n')
# 	for employeeRecord in employees:
# 			print('{0}\t{1}\t\t{2}\t{3}'.format(employeeRecord[0], employeeRecord[1], employeeRecord[2], employeeRecord[3]))

# def read():
# 	conn = sqlite3.connect('employees.sqlite')

# 	cursor = conn.cursor()

# 	query = '''
# 	    SELECT ID, NAME, AGE, SALARY FROM EMPLOYEE;
# 	'''
# 	try: 
# 		cursor.execute(query)
# 		employeeData = cursor.fetchall()
# 		conn.commit()
# 	except:
# 		cursor = conn.cursor()
# 		query = ('''CREATE TABLE EMPLOYEE(ID INTEGER PRIMARY KEY NOT NULL,
# 										NAME TEXT NOT NULL,
# 										AGE INTEGER NOT NULL,
# 										SALARY INTEGER NOT NULL
# 										);''')

# 		cursor.execute(query)
# 		conn.commit()

# 	conn.close()
# 	return employeeData

# showData()




























# import sqlite3

# def create_table():

# 	conn = sqlite3.connect('employees.sqlite')
# 	cursor = conn.cursor()
# 	query = ('''CREATE TABLE EMPLOYEE(ID INTEGER PRIMARY KEY NOT NULL,
# 									NAME TEXT NOT NULL,
# 									AGE INTEGER NOT NULL,
# 									SALARY INTEGER NOT NULL
# 									);''')

# 	cursor.execute(query)
# 	conn.commit()
# 	conn.close()


# def insert():
# 		ID = int(input("Enter ID: "))
# 		NAME = input("Enter Name: ")
# 		AGE = int(input("Enter Age: "))
# 		SALARY = int(input("Enter Salary: "))
# 		insert_records(ID, NAME, AGE, SALARY)

# def insert_records(ID, NAME, AGE, SALARY):
	
# 	conn = sqlite3.connect('employees.sqlite')

# 	cursor = conn.cursor()

# 	query = '''INSERT INTO EMPLOYEE(ID, NAME, AGE, SALARY)
# 	    	        VALUES ( ?,?,?,? )
# 										'''

# 	cursor.execute(query,(ID, NAME, AGE, SALARY))

# 	conn.commit()
# 	conn.close()


# def showData():
# 	employees = read()
# 	print('\nID\tNAME\t\tAGE\tSALARY\n')
# 	for employeeRecord in employees:
# 			print('{0}\t{1}\t\t{2}\t{3}'.format(employeeRecord[0], employeeRecord[1], employeeRecord[2], employeeRecord[3]))

# def read():
# 	conn = sqlite3.connect('employees.sqlite')

# 	cursor = conn.cursor()

# 	query = '''
# 	    SELECT ID, NAME, AGE, SALARY FROM EMPLOYEE;
# 	'''

# 	cursor.execute(query)
# 	employeeData = cursor.fetchall()

# 	conn.commit()
# 	conn.close()
# 	return employeeData



# def show_data_by_id(ID):
# 	employees = get_employee_by_id(ID)
# 	if not employees:
# 		print("No data found at id", ID)
# 	else:
# 		print('\nID\tNAME\t\tAGE\tSALARY\n')
# 		for employeeRecord in employees:
# 			print('\n{0}\t{1}\t\t{2}\t{3}'.format(employeeRecord[0], employeeRecord[1], employeeRecord[2], employeeRecord[3]))


# def get_employee_by_id(ID):
# 	conn = sqlite3.connect('employees.sqlite')

# 	cursor = conn.cursor()

# 	query = '''
# 	    SELECT ID, NAME, AGE, SALARY
# 	    FROM EMPLOYEE
# 	    WHERE ID = {}
# 	''' .format(ID)

# 	cursor.execute(query)
# 	employeeData = cursor.fetchall()

# 	conn.commit()
# 	conn.close()

# 	return employeeData



# def update():
# 		ID = int(input('Enter Id: '))
# 		show_data_by_id(ID)
# 		NAME = input('Name: ')
# 		AGE = int(input('Age: '))
# 		SALARY = int(input('Salary: '))
# 		update_employee(ID, NAME, AGE, SALARY)


# def update_employee(ID, NAME, AGE, SALARY):
# 	conn = sqlite3.connect('employees.sqlite')

# 	cursor = conn.cursor()

# 	query = '''
# 	    UPDATE EMPLOYEE
# 	    SET NAME = ?, AGE = ?, SALARY = ?
# 	    WHERE ID = ?
# 	'''

# 	cursor.execute(query,(NAME, AGE, SALARY, ID))

# 	conn.commit()
# 	conn.close()






# def delete():
# 		ID = int(input('Enter Id: '))
# 		show_data_by_id(ID)
# 		delete_employee(ID)


# def delete_employee(ID):
# 	conn = sqlite3.connect('employees.sqlite')

# 	cursor = conn.cursor()

# 	query = '''
# 	    DELETE
# 	    FROM EMPLOYEE
# 	    WHERE ID = {}
# 	''' .format(ID)

# 	cursor.execute(query)
# 	employeeData = cursor.fetchall()

# 	conn.commit()
# 	conn.close()

# 	return employeeData
	


# def search():
# 		ID = int(input("Enter ID: "))
# 		show_data_by_id(ID)





# # create_table()

# while True:
# 	print("\n------------- EMPLOYEE RECORD MANAGEMENT -------------\n")
# 	print("Please choose: \n1. Add New employeeRecord\n2. Show all employees\n3. Update an employeeRecord\n4. Delete an employeeRecord\n5. Search an employeeRecord\n6. exit\n")
# 	print("-------------------------------------------------------")
# 	[insert, showData, update, delete, search, exit][int(input("\nEnter your choice: "))-1]()	

	



















