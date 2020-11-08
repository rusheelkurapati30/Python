# program on weather_report to check the temperature of a given location.

import requests
locationName = input("\nEnter location name : ")
url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=4167ebf679542684b2a0cb8a58701c27&units=metric"  % (locationName)  
response = requests.get(url)
weatherReportData = eval(response.text)
if weatherReportData["cod"] != '404':
    print("\nTemperature in " + locationName + " is: " + str(weatherReportData["main"]["temp"])  + "C.\n")
else:
    print("\nLocation not found.\n")
























# import os 
# locationName = ""

# def saveWeatherLocationDataIntoFile():
# 	locationName = input("\nEnter Location Name: ") 
# 	url = "curl -s \"https://api.openweathermap.org/data/2.5/weather?q=%s&appid=4167ebf679542684b2a0cb8a58701c27&units=metric\" > weatherReport.dat" % (locationName)
# 	os.system(url)

# saveWeatherLocationDataIntoFile()

# def checkTemperature():
# 	File = open("weatherReport.dat", "r")
# 	weatherReport = File.readlines()
# 	weatherReportData = str(weatherReport)
# 	tempLocationPointer = weatherReportData.find("temp")
# 	print("\nTemperature in " + locationName + " is: " + weatherReportData[tempLocationPointer+6:tempLocationPointer+11] +"C.")

# checkTemperature()











# import re
# import os
# cityName= input("Enter city name : ") 
# url = "curl -s \"https://api.openweathermap.org/data/2.5/weather?q=%s&appid=4167ebf679542684b2a0cb8a58701c27&units=metric\" > weatherReport.dat" % (cityName)
# os.system(url)
# File = open("weatherReport.dat", "r")
# weatherReportData = File.readlines()
# print(weatherReportData)
# print()
# convert = str(weatherReportData)
# print(convert)
# keys = convert.keys() 
# values = convert.values() 
  
# # printing keys and values separately 
# print ("keys : ", str(keys)) 
# print ("values : ", str(values))


# splitt = convert.split()
# print(splitt[141:145])

# names = "rusheel raju rahul"
# print(names)
# print(names.split())
# print(names[0])




# print(convert[141:146])
# extracted = convert.get('main')n
# print(extracted)
# print ("Temp : " + convert[141:145] + "C.")
# print((weatherReportData[5:25]))
# weatherReportData = {"coord":{"lon":78.47,"lat":17.38},"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"},{"id":721,"main":"Haze","description":"haze","icon":"50d"}],"base":"stations","main":{"temp":302.11,"feels_like":306.81,"temp_min":302.04,"temp_max":302.15,"pressure":1006,"humidity":79},"visibility":5000,"wind":{"speed":2.41,"deg":198},"rain":{"1h":3.16},"clouds":{"all":75},"dt":1599819914,"sys":{"type":1,"id":9214,"country":"IN","sunrise":1599784427,"sunset":1599828719},"timezone":19800,"id":1269843,"name":"Hyderabad","cod":200}
# # convert = eval(weatherReportData)
# extracted = weatherReportData.get('main')
# print(extracted)
# keys = extracted.keys() 
# values = extracted.values() 
  
# # printing keys and values separately 
# print ("keys : ", str(keys)) 
# print ("values : ", str(values))

# print(values[5]) 
# for lines in extracted:
# 	print(lines)	

# string = str(extracted)
# print(string[1:15])

# # # print("CURL \"https://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid=4167ebf679542684b2a0cb8a58701c27\" > weatherReport.dat")
# # # import os
# # # url = "curl -s \"https://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid=4167ebf679542684b2a0cb8a58701c27\" > weatherReport.dat"
# # # os.system(url)
# # # File = open("weatherReport.dat", "r")
# # # weatherReportData = File.readlines()
# # # # for lines in len(weatherReportData):
# # # print(len(weatherReportData))
# # # print(weatherReportData)


# import os
# import re
# url = "curl -s \"https://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid=4167ebf679542684b2a0cb8a58701c27\" > weatherReport.dat"
# os.system(url)
# File = open("weatherReport.dat", "r")
# weatherReportData = File.readlines()
# # for lines in len(weatherReportData):
# # print(len(weatherReportData))
# # print(str(weatherReportData))
# # # myLine="This is;a-line,with pieces"
# # for line in re.split("[,]", weatherReportData):
# #     print(line)
# for lines in weatherReportData[2:15]:
# 	print(lines)

# import json
 # myLine="This is;a-line,with pieces"
# for line in re.split("[,]", extracted):
#     print(line)









# # weather = str(weatherReportData)
# # print(type(weatherReportData))
# # print(str(weatherReportData))
# # print(type(weatherReportData))
# # print(weatherReportData)
# # print(re.split(':,[{', weatherReportData))

# # ni_dict = {'a' : 'akshat', 'b' : 'bhuvan', 'c': 'chandan'} 

# weatherReportData= {"coord":{"lon":78.47,"lat":17.38},"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"},{"id":721,"main":"Haze","description":"haze","icon":"50d"}],"base":"stations","main":{"temp":302.11,"feels_like":306.81,"temp_min":302.04,"temp_max":302.15,"pressure":1006,"humidity":79},"visibility":5000,"wind":{"speed":2.41,"deg":198},"rain":{"1h":3.16},"clouds":{"all":75},"dt":1599819914,"sys":{"type":1,"id":9214,"country":"IN","sunrise":1599784427,"sunset":1599828719},"timezone":19800,"id":1269843,"name":"Hyderabad","cod":200}

#  weatherReportData = str(weatherReport)
# # printing iniial_dictionary 
# # print("intial_dictionary", str(weatherReportData)) 
  
# # split dictionary into keys and values










# import os 
# locationName= input("\nEnter Location Name: ") 
# url = "curl -s \"https://api.openweathermap.org/data/2.5/weather?q=%s&appid=4167ebf679542684b2a0cb8a58701c27&units=metric\" > weatherReport.dat" % (locationName)
# os.system(url)
# File = open("weatherReport.dat", "r")
# weatherReport = File.readlines()
# # print(weatherReport)
# # print()
# weatherReportData = str(weatherReport)
# tempLocationPointer = weatherReportData.find("temp")
# # print(findTheTemp)
# # print("temp found at : " + str(findTheTemp))
# print("\nTemperature in " + locationName + " is: " + weatherReportData[tempLocationPointer+6:tempLocationPointer+11] +"C.")
# print(weatherReportData[findTheTemp+6:findTheTemp+11])








# print(weatherReport[0][0:488])
# print(weatherReport[0][0:488])
# if 
# keys = weatherReportData.keys() 
# values = weatherReportData.values() 

# converted = convert.get('main')
# print(converted)
# for line in convert.items():
# 	print(str(line[0]) + ": " + str(line[1]))

# for keys, values in weatherReportData.items():
  	# print(keys, values)

# # printing keys and values separately 
# print ("keys : ", keys) 
# print ("values : ", values)
