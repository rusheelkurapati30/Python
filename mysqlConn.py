import mysql.connector

conn = mysql.connector.connect(
	host="165.22.14.77",
	user="rusheel",
	password="rusheel",
	database="dbRusheel"
	)

mycursor = conn.cursor()

mycursor.execute("select * from Items")
# mycursor.execute("SHOW TABLES")

for x in mycursor:
	print(x)
