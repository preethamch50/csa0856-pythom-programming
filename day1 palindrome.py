#Given an integer x, return true if x is palindrome integer.
string1= input("Enter the integer: ")
string2=string1[::-1]
if string1==string2:
    print("True")
else:
    print("False")

#Output:
#Enter the integer: -121
#False
