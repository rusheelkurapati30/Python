# Program to send an email through python.

import smtplib

server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)

print("\nSign in")
senderEmail = input("\nEmail: ")
password = input("\nPassword: ")
server.login(senderEmail, password)
print("\nLogin success")

receiverEmail = input("\nEnter receiver email ID:")

message = input("\nEnter message: ")

server.sendmail(senderEmail, receiverEmail, message)

print("\nMessage sent.")

server.quit()