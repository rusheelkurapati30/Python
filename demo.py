# print("-" * 50)


# delim = ", "
# a = {"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"base":"stations","main":{"temp":18.7,"feels_like":14.54,"temp_min":17.22,"temp_max":19.44,"pressure":1017,"humidity":48},"visibility":10000,"wind":{"speed":5.1,"deg":240},"clouds":{"all":40},"dt":1599828796,"sys":{"type":1,"id":1414,"country":"GB","sunrise":1599802181,"sunset":1599848683},"timezone":3600,"id":2643743,"name":"London","cod":200}
# splitt = a.split(delim)
# print(split)


# import requests, json 
# locationName = input("Enter location name : ") 
# url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=4167ebf679542684b2a0cb8a58701c27&units=metric"  % (locationName)  
# response = requests.get(url) 
# x = response.json() 
# if x["cod"] != "404": 
#     y = x["main"] 
#     current_temperature = y["temp"] 
#     z = x["weather"] 
#     weather_description = z[0]["description"] 
#     print(" Temperature in " + locationName + " is: " + str(current_temperature) + "C.")
# else: 
# #     print(" City Not Found ") 


# import requests
# app_id = "cd9f1a0d"
# app_key = "1f766ec01c258b21809ed532ff88579f"
# language = "en-gb"
# word_id = "Believe"
# headers = {'app_id': app_id, 'app_key': app_key}
# url_mean = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
# r_mean = requests.get(url_mean, headers=headers)
# if r_mean:
#     mean_json = r_mean.json()
#     mean_list = []
#     for result in mean_json['results']:
#         for lexicalEntry in result['lexicalEntries']:
#             for entry in lexicalEntry['entries']:
#                 for sense in entry['senses']:
#                     mean_list.append(sense['definitions'][0])
#     print("Following are the list of meanings available for the search : " + word_id)
#     for i in mean_list:
#         print(i)
# else:
#     print("No matches found.. \n Please try again with different word")





# Python program to create a simple XLSX file and adding an embedded chart.

# import xlsxwriter
# # sheets = ['EmployeeData', 'StudentData']
# # for sheet in range(len(sheets)):
# workbook = xlsxwriter.Workbook('xlsxEmpData.xlsx')
# 	# print(sheets[sheet])
# worksheet = workbook.add_worksheet('EmployeeData')


# chart = workbook.add_chart({'type': 'line'})

# bold = workbook.add_format({'bold': True})

# worksheet.set_column('A:A', 15)
# worksheet.set_column('B:B', 15)
# worksheet.set_column('C:C', 15)

# fieldNames = ["Employee Name", "Joining Date", "Employee Salary"]

# worksheet.write('A1', fieldNames[0], bold)
# worksheet.write('B1', fieldNames[1], bold)
# worksheet.write('C1', fieldNames[2], bold)

# row = 1
# def addRecords():
# 	global row
# 	global employeeData
# 	employeeData = []
# 	newData = []
# 	for counter in range(len(fieldNames)):
# 		empData = input("\nEnter " + fieldNames[counter] + ": ")
# 		employeeData.append(empData)
# 		worksheet.write(row, counter, str(employeeData[counter]))
# 	row += 1
# 	choice = input("\nDo you want to add one more record? [y/n]")
# 	if choice.upper() == 'Y':
# 		addRecords()

# addRecords()

# chart.add_series({'values': '=EmployeeData!$C$2:$C$4'})

# chart.set_x_axis({'name': 'Earnings per Month'})

# worksheet.insert_chart('E1', chart)


# workbook.close()





# # Python program to create a simple XLSX file and adding an embedded chart.

# # from datetime import datetime
# import xlsxwriter


# workbook = xlsxwriter.Workbook('xlsxEmpData1.1.xlsx')
# worksheet = workbook.add_worksheet()

# chart = workbook.add_chart({'type': 'column'})

# bold = workbook.add_format({'bold': True})

# # date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

# worksheet.set_column('A:A', 15)
# worksheet.set_column('B:B', 15)
# worksheet.set_column('C:C', 15)

# fieldNames = ["Employee Name", "Joining Date", "Employee Salary"]

# worksheet.write('A1', fieldNames[0], bold)
# worksheet.write('B1', fieldNames[1], bold)
# worksheet.write('C1', fieldNames[2], bold)

# employeeData = []
# newData = []

# # row = 1
# # column = 0

# # for employeeName, d, employeeSalary in (employeeData):
# #     # date = datetime.strptime(date_str, "%Y-%m-%d")

# #     worksheet.write_string  (row, column,     employeeName              )
# #     worksheet.write_datetime(row, column + 1, date, date_format )
# #     worksheet.write_number  (row, column + 2, employeeSalary)
# #     row += 1

# # worksheet.write(row, 0, 'Total', bold)
# # worksheet.write(row, 2, '=SUM(C2:C5)')


# # chart.add_series({'values': '=Sheet1!$B$2:$B$5'})
# chart.add_series({'values': '=Sheet1!$C$2:$C$5'})

# chart.set_x_axis({'name': 'Earnings per Month'})

# worksheet.insert_chart('A10', chart)

# def addRecords():
# 	row = 0
# 	for counter in range(len(fieldNames)):
# 		row += 1
# 		empData = input("\nEnter " + fieldNames[counter] + ": ")
# 		newData.append(empData)
# 		worksheet.write(row, counter, str(newData[counter]))
# 	choice = input("\nDo you want to add one more record? [y/n]")
# 	if choice.upper() == 'Y':
# 		# totalData.append(newData)
# 		# print(totalData)	
# 		addRecords()


# addRecords()
# # row = 1

# workbook.close()





# import xlsxwriter

# workbook = xlsxwriter.Workbook("sample.xlsx")
# worksheet = workbook.add_worksheet()

# data = [10, 30, 40, 50, 80, 60]

# worksheet.write_column('A1', data)

# chart = workbook.add_chart({'type': 'line'})

# chart.add_series({'values': '=Sheet1!$A$1:$A$6'})

# worksheet.insert_chart('C1', chart)

# workbook.close()