#Valid Palindrome A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads the same forward
and backward. Alphanumeric characters include letters and numbers. Given a string s, return
true if it is a palindrome, or false otherwise.
SOL:

def isPalindrome(s):
 s1 = s.replace(' ', '')
 s1 = s1.lower()
 s2 = s1[::-1];
 return True if s1 == s2 else False
s = input("string is:")
if (isPalindrome(s)):
 print ("Sentence is palindrome.")
else:
 print ("Sentence is not palindrome.") 
