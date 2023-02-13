#Write a program to find the number of student users in the college, get the total users, staff
users details from the client. Note for every 3 staff user there is one Non-teaching staff user
assigned by default.
SOL:

total=int(input("enter the total number of users"))
if(total<=0):
 print("invalid")
else:
 sf=int(input("enter the number of staff users"))
 if(sf>total):
 print("invalid")
 elif(sf==total):
 print("invalid")
 else:
 nsf=sf/3
 su=total-sf-nsf
 print("the total number of staff users is",su)
