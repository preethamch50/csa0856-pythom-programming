#Longest Substring with At Least K Repeating Characters. Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
Sol:
def Substring(s):
    ans, temp = 1, 1
    for i in range(1, len(s)):
        if (s[i] == s[i - 1]):
            temp += 1
        else:
            ans = max(ans, temp)
            temp = 1
 
    ans = max(ans, temp)
    return ans

s = input("Enter the string: ")
print(Substring(s))

Output:
Enter the string: aaabb
3
