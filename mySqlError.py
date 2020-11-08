#Python program to connect MySql and show the error message if Sold Quantity is inserted more than Stock Quantity.
import mysql.connector

conn = mysql.connector.connect(
	host="165.22.14.77",
	user="rusheel",
	password="rusheel",
	database="dbRusheel"
	)
cursor = conn.cursor();

def Insert_Into_Bill_Detail():
	try:
		Bill_Number = input("\nEnter Bill Number: ")
		Item_ID = input("\nEnter Item ID: ")
		Sold_Quantity = int(input("\nEnter Sold Quantity: "))
		print()
		query = "INSERT INTO Bill_Detail(Bill_Number, Item_ID, Sold_Quantity) VALUES('{}', '{}', {})" .format(Bill_Number, Item_ID, Sold_Quantity)
		cursor.execute(query)
	
		conn.commit()	
	
	except:
		Print_Error_Message(45000)

def Print_Error_Message(errorNo):
	query = "SELECT Description FROM ERROR WHERE ErrorNo = errorNo";
	cursor.execute(query)
	message = cursor.fetchall()
	print(message[0][0])

Insert_Into_Bill_Detail()
