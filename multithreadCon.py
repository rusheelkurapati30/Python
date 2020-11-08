#Program to print odd and even numbers.

# maximum = int(input("\nPlease enter maximum value to print even and odd numbers: "))
# for number in range(1, maximum+1):
# 	if number % 1 == 0:
# 		print(number)
# 	else:
# 		print(number)




#Program to print odd and even numbers.

# maximum = int(input("\nPlease enter any maximum value to print even and odd numbers: "))

# def odd():
# 	for oddNumber in range(1, maximum + 1, 2):
# 		print(oddNumber)

# def even():
# 	for evenNumber in range(2, maximum + 1, 2):
# 		print(evenNumber)

# odd()
# even()




#Program to print odd and even numbers using threads.

import threading
import time

maximum = int(input("\nPlease enter any maximum value: "))

def odd():
	for oddNumber in range(1, maximum + 1, 2):
		print(oddNumber)
		time.sleep(0.2)

def even():
	for evenNumber in range(2, maximum + 1, 2):
		print(evenNumber)
		time.sleep(0.2)

def threadStart():
	try:
		thread1 = threading.Thread(target = odd)
		thread1.start()
		time.sleep(0.1)
		thread2 = threading.Thread(target = even)
		thread2.start()
	except:
		print("Error!")
	
threadStart()






CREATE FUNCTION printName(
	name varchar(20)
	)
RETURNS SELECT name from dual