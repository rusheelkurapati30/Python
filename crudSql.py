#Python program to perform CRUD operations using MYSQL Connector.
import mysql.connector

conn = mysql.connector.connect(
	host="165.22.14.77",
	user="rusheel",
	password="rusheel",
	database="dbRusheel"
	)

cursor = conn.cursor()

def insert():
	try:
		while True:
			Item_ID = input("\nEnter Item ID: ")
			Item_Description = input("\nEnter Item Description: ")
			Unit_Price = float(input("\nEnter Unit Price: "))
			Stock_Quantity = int(input("\nEnter Stock Quantity: "))
			Supplier_ID = input("\nEnter Supplier ID: ")
			
			query = "INSERT INTO Items(Item_ID, Item_Description, Unit_Price, Stock_Quantity, Supplier_ID) VALUES('{}','{}',{},{},'{}')" .format(Item_ID, Item_Description, Unit_Price, Stock_Quantity, Supplier_ID)
			cursor.execute(query)

			conn.commit()

			choice = input("\nDo you want to continue? [y/n] ")
			if (choice.upper() != 'Y'):
					break
	except Exception as e:
		print(e)
		# print("Insert Valid Data")
		conn.rollback()



def showData():
	try:
		query = "SELECT Item_ID, Item_Description, Unit_Price, Stock_Quantity, Supplier_ID FROM Items ";
		cursor.execute(query)
		ItemData = cursor.fetchall()

		if ItemData:
			printData(ItemData)
			conn.commit()
		else:
			print("\nNo records found.")
			conn.rollback()
	except:
		printIfTableIsNotAvailable()
	

def printData(ItemData):
	print("\nItem_ID\t\tItem_Description\t\tUnit_Price\t\tStock_Quantity\tSupplier_ID\n")
	for ItemRecord in ItemData:
		print('{0}\t\t{1}\t\t\t{2}\t\t\t{3}\t\t{4}'.format(ItemRecord[0], ItemRecord[1], ItemRecord[2], ItemRecord[3], ItemRecord[4]))


def showDataByID(Item_ID):
	try:
		global recordFound
		recordFound = 0
		query = '''SELECT Item_ID, Item_Description, Unit_Price, Stock_Quantity, Supplier_ID FROM Items WHERE  Item_ID = "{}"''' .format(Item_ID)
		cursor.execute(query)
		ItemData = cursor.fetchall()

		conn.commit()

		if ItemData:
			recordFound += 1
			printData(ItemData)
		else:
			print("\nNo record found with Item ID: ", Item_ID + ".")
	except:
		printIfTableIsNotAvailable()

	
def printIfTableIsNotAvailable():
	print("\nNo Table is Available.")


def update():
	Item_ID = input("\nEnter Item ID to Update: ")
	showDataByID(Item_ID)
	if recordFound == 1:
		print("\n1. To Update Item Description")
		print("2. To Update Unit Price")
		print("3. To Update Stock Quantity")

		choice = int(input("\nEnter your choice: "))

		if choice == 1:
			Item_Description = input("\nEnter Item Description to Update: ")
			query = "UPDATE Items SET Item_Description = '{}' WHERE Item_ID = '{}'" .format(Item_Description, Item_ID)
			cursor.execute(query)
		if choice == 2:
			Unit_Price = float(input("\nEnter Unit Price to Update: "))
			query = "UPDATE Items SET Unit_Price = {} WHERE Item_ID = '{}'" .format(Unit_Price, Item_ID)
			cursor.execute(query)
		if choice == 3:
			Stock_Quantity = int(input("\nEnter Stock Quantity to Update: "))
			query = "UPDATE Items SET Stock_Quantity = {} WHERE Item_ID = '{}'" .format(Stock_Quantity, Item_ID)
			cursor.execute(query)

		conn.commit()
		print("\nRecord updated.")



def delete():
	try:
		Item_ID = input("\nEnter Item ID to Delete: ")
		query = "SELECT Item_ID FROM Items WHERE Item_ID = '{}'" .format(Item_ID)
		cursor.execute(query)
		ItemData = cursor.fetchone()
		if ItemData:
			query = "Delete FROM Items WHERE Item_ID = '{}'" .format(Item_ID)
			cursor.execute(query)
			conn.commit()
			print("\nRecord deleted.")
		else:
			print("\nNo record found")	
	except:
		printIfTableIsNotAvailable()

def search():
	Item_ID = input("\nEnter Item ID to Search: ")
	showDataByID(Item_ID)
	

def exitProgram():
	conn.close()
	exit(0)


while True:
	print("\n--------------Big Bazar Item Details--------------")
	print("\nPlease choose: \n1. Add New item\n2. Show all items\n3. Update an item\n4. Delete an item\n5. Search an item\n6. exit\n")
	print("-" * 50)
	[insert, showData, update, delete, search, exitProgram][int(input("\nEnter your choice: "))-1]()


