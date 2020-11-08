# Python program to create a simple XLSX file and adding an embedded chart.

from datetime import datetime
import xlsxwriter


workbook = xlsxwriter.Workbook('xlsxEmpData1.xlsx')
worksheet = workbook.add_worksheet("Employeedata")

chart = workbook.add_chart({'type': 'column'})

bold = workbook.add_format({'bold': True})

# date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

worksheet.set_column('A:A', 15)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 15)

fieldNames = ["Employee Name", "Joining Date", "Employee Salary"]

worksheet.write('A1', fieldNames[0], bold)
worksheet.write('B1', fieldNames[1], bold)
worksheet.write('C1', fieldNames[2], bold)

# workbook.close()
row = 1
def addRecords():
	global row
	global newData
	global totalData
	totalData = []
	newData = []
	for counter in range(len(fieldNames)):
		empData = input("\nEnter " + fieldNames[counter] + ": ")
		newData.append(empData)
		worksheet.write(row, counter, str(newData[counter]))
	row += 1
	choice = input("\nDo you want to add one more record? [y/n]")
	if choice.upper() == 'Y':
		totalData.append(newData)
		# print(totalData)
		addRecords()

addRecords()


# chart.add_series({'values': '=Sheet1!$B$2:$B$5'})
chart.add_series({'values': '=Employeedata!$C$2:$C$4'})

chart.set_x_axis({'name': 'Earnings per Month'})

worksheet.insert_chart('A10', chart)


workbook.close()






# # Python program to create a simple XLSX file and adding an embedded chart.

# from datetime import datetime
# import xlsxwriter


# workbook = xlsxwriter.Workbook('xlsxEmpData1.xlsx')
# worksheet = workbook.add_worksheet()

# chart = workbook.add_chart({'type': 'column'})

# bold = workbook.add_format({'bold': True})

# date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

# worksheet.set_column('A:A', 15)
# worksheet.set_column('B:B', 15)
# worksheet.set_column('C:C', 15)

# fieldNames = [Employee Name, Joining Date, Employee Salary]

# worksheet.write('A1', 'Employee Name', bold)
# worksheet.write('B1', 'Joining Date', bold)
# worksheet.write('C1', 'Employee Salary', bold)


# employeeData = ()
#     # ['Rusheel', '2020-09-01', 15000],
#     # ['Dinesh', '2020-08-09', 20000],
#     # ['Raju', '2020-07-09', 17000],
#     # ['Somesh', '2020-06-10', 21000],
# newData = []
# for field in fieldNames:
# 	for counter in range(len(field)):
# 		data = input("\nEnter " + field[1])
# 		newData.append(data)
# print(newData)


# row = 1
# column = 0

# for employeeName, date_str, employeeSalary in (employeeData):
#     date = datetime.strptime(date_str, "%Y-%m-%d")

#     worksheet.write_string  (row, column,     employeeName              )
#     worksheet.write_datetime(row, column + 1, date, date_format )
#     worksheet.write_number  (row, column + 2, employeeSalary)
#     row += 1

# worksheet.write(row, 0, 'Total', bold)
# worksheet.write(row, 2, '=SUM(C2:C5)')


# # chart.add_series({'values': '=Sheet1!$B$2:$B$5'})
# chart.add_series({'values': '=Sheet1!$C$2:$C$5'})

# chart.set_x_axis({'name': 'Earnings per Month'})

# worksheet.insert_chart('A10', chart)


# workbook.close()
