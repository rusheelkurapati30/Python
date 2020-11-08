File = open("databaseFile.dat", "r")
listOfFields = ['Name', 'Age']
listOfNames = []
listOfNames = File.readlines()
print(listOfNames)
for index in range(len(listOfNames)):
	if index % len(listOfFields) == 0:
		for counter in range(len(listOfFields)):
			print(listOfFields[counter] + ": " + listOfNames[index + counter], end = "")
		print()