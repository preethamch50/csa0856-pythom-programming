#Write a function delchar(s,c) that takes as input strings s and c, where c has length 1 (i.e., a
single character), and returns the string obtained by deleting all occurrences of c in s. If c has
a length other than 1, the function should return s.


input_string = input("enter the string")
char_to_remove = input("enter the character")
newStr = ""
for character in input_string:
 if character != char_to_remove:
 newStr += character
print("The input string is:", input_string)
print("The character to delete is:", char_to_remove)
print("The output string is:", newStr)
