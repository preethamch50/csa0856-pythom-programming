#Scramble String We can scramble a string s to get a string t using the following algorithm: If
the length of the string is 1, stop. If the length of the string is > 1, do the following: Split the
string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x
and y where s = x + y. Randomly decide to swap the two substrings or to keep them in the
same order. i.e., after this step, s may become s = x + y or s = y + x. Apply step 1 recursively
on each of the two substrings x and y. Given two strings s1 and s2 of the same length, return
true if s2 is a scrambled string of s1, otherwise, return false.
SOL:

def isScramble(S1: str, S2: str):
 if len(S1) != len(S2):
 return False
 n = len(S1)
 if not n:
 return True
 if S1 == S2:
 return True
 if sorted(S1) != sorted(S2):
 return False
 for i in range(1, n):
 if (isScramble(S1[:i], S2[:i]) and
 isScramble(S1[i:], S2[i:])):
 return True
 if (isScramble(S1[-i:], S2[:i]) and
 isScramble(S1[:-i], S2[i:])):
 return True
 return False
if _name_ == "_main_":
 S1 = "GREAT"
 S2 = "RGEAT
 if (isScramble(S1, S2)):
 print("True")
 else:
 print("False")
