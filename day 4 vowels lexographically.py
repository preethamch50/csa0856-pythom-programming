#Count Sorted Vowel Strings Given an integer n, return the number of strings of length n that
consist only of vowels (a, e, i, o, u) and are lexicographically sorted. A string s is
lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the
alphabet.

SOL:
def countstrings(n, start):
 if n == 0:
 return 1
 cnt = 0
 for i in range(start, 5):
 cnt += countstrings(n - 1, i)
 return cnt
def countVowelStrings(n):
 return countstrings(n, 0)
n =int(input("enter the value of n:"))
print(countVowelStrings(n)) 
