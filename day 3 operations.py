#Given two strings word1 and word2, return the minimum number of
#operations required to convert word1 to word2. You have the following
#three operations permitted on a word: 
•Insert a character 
•Delete a character 
•Replace a character
Program:
def editDistance(str1, str2, m, n):
   if m == 0:
        return n
  if n == 0:
        return m
 if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)
 return 1 + min(editDistance(str1, str2, m, n-1),    # Insert
                   editDistance(str1, str2, m-1, n),    # Remove
                   editDistance(str1, str2, m-1, n-1)    # Replace
                   )
 # Driver code
str1 = "sunday"
str2 = "saturday"
print (editDistance(str1, str2, len(str1), len(str2)))

Output:
Input: word1 = "horse", word2 = "ros" 
Output: 3 
