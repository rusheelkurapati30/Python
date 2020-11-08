// Write a C program to run a Python program using command line arguments.

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
char mobileNumber[12];
char command[50];
void main(int argcount, char *arglist[])
{
	if(argcount == 1)
	{
		printf("\nEnter your mobile number to receive OTP: ");
		scanf("%s", mobileNumber);
	}
	if(argcount == 2)
	{
		strcpy(mobileNumber, arglist[1]);
	}
	if(argcount > 2)
	{
		printf("\nUsage: <executable file name> <mobileNumber>");
		exit(0);
	}
	sprintf(command, "python sendOtp.py %s", mobileNumber);
	system(command);
// system("python sendOtp.py 7287068516 hi how are you");
}
