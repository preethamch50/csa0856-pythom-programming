#Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

Sol:
s=input("Enter the string:")
s1=s.split()
n=len(s1)
print("Number of words: ",n)
print("Last word: ",s1[n-1], len(s1[n-1]))

Output:
Enter the string: Welcome to Python Programming
Number of words:  4
Last word:  Programming 11
