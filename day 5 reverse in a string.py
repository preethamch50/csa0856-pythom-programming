#Reverse Words in a String. Given an input string s, reverse the order of the words.
Sol:
str1=input("Enter the string: ")
str2=str1.split()[::-1]
print(*str2)

Output:
Enter the string: The sky is blue
blue is sky The
