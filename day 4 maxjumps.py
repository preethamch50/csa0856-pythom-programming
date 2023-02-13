#Given an array of integers where each element represents the max number of steps that can
be made forward from that element. Write a function to return the minimum number of
jumps to reach the end of the array (starting from the first element). If an element is 0, they
cannot move through that element. If the end isn’t reachable, return -1.
SOL:

def minJumps(arr, l, h):
 if (h == l):
 return 0
 if (arr[l] == 0):
 return float('inf')
 min = float('inf')
 for i in range(l + 1, h + 1):
 if (i < l + arr[l] + 1):
 jumps = minJumps(arr, i, h)
 if (jumps != float('inf') and
 jumps + 1 < min):
 min = jumps + 1
 return min
arr = []
m=int(input("enter the limit for the list"))
for s in range(m):
 lis=int(input())
 arr.append(lis)
 print()
n = len(arr)
print('Minimum number of jumps to reach',
 'end is', minJumps(arr, 0, n-1)) 
