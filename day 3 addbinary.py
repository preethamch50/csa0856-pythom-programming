#Add Binary 
Given two binary strings a and b, return their sum as a binary string. 
• a and b consist only of '0' or '1' characters. 
• Each string does not contain leading zeros except for the zero itself

Program:
b1=input("enter the string:")
b2=input("enter the string:")
sum = bin(int(b1,2) + int(b2,2))
print(sum[2:])
#Output:
Input: a = "11", b = "1" 
Output: "100" 
