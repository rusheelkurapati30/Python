# Python program to announce the status of a train.

from playsound import playsound

announcement = []

def enterTrainNumber():
	trainNumber = input("\nEnter train number: ")
	if len(trainNumber) == 5 and trainNumber.isnumeric():
		for number in trainNumber:
			announcement.append(number)
	else:
		print("\nPlease enter valid train number.")
		exit()

def enterPlatformNumber():
	platformNum = input("\nEnter platform number: ")
	if platformNum.isnumeric():
		announcement.append(platformNum)
		makeAnnouncement()
	else:
		print("\nPlease enter valid platform number.")
		exit()

def makeAnnouncement():
	print("Train status.....")
	for counter in range(len(announcement)):
		playsound(announcement[counter] + ".mp3")

		
announcement.append("trainNumber")
enterTrainNumber()
announcement.append("willArrive")
enterPlatformNumber()