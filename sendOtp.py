# Python program to generate and validate OTP.

import sys
import random
import requests
def verifyOtp():
	otp = ''
	for counter in range(6):
		generatedOtp += str(random.randint(0, 9))

	message = "Your OTP is " + otp + "."

	mobileNumber = sys.argv[1]

	url = "http://psms.goforsms.com/API/sms.php?username=srushtiimages&password=tecnics&from=WEBSMS&to=%s&msg=%s&type=1&dnd_check=0" % (mobileNumber, message)
	response = requests.get(url)

	otpVerification = input("\nPlease enter OTP to login: ")
	if otpVerification == generatedOtp:
		print("\nlogin successful.") 
	else:
		print("\nThe OTP entered is incorrect.")
		exit(0)

verifyOtp()




# import sys
# import random
# import requests

# def sendMessage():
# 	# print(len(sys.argv))
# 	if  (sys.argv[1].isdigit()):
# 		mobileNumber = sys.argv[1]
# 		for length in range(3, len(sys.argv)):
# 			sys.argv[2] += " " + sys.argv[length]

# 		message = sys.argv[2]

# 	else:
# 		mobileNumber = input("\nEnter your mobile number: ")
# 		message = input("\nEnter message: ")
# 	# url = "http://psms.goforsms.com/API/sms.php?username=srushtiimages&password=tecnics&from=WEBSMS&to=%s&msg=%s&type=1&dnd_check=0" % (mobileNumber, message)
# 	# response = requests.get(url)
# 	print(mobileNumber)
# 	print(message)

# sendMessage()




# if len(sys.argv) == 6 and sys.argv[1].isdigit():
# 		mobileNumber = sys.argv[1]
# 		for length in range(3, len(sys.argv)):
# 			sys.argv[2] += " " + sys.argv[length]

# 		message = sys.argv[2]