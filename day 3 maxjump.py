#Given an array of integers where each element represents the max number
#of steps that can be made forward from that element. Write a function to
#return the minimum number of jumps to reach the end of the array
#(starting from the first element). If an element is 0, they cannot 
move through that element. If the end isn’t reachable, return -1. 
Program:
def jump(a):
    jump, currEnd, nextEnd = 0, 0, 0
    for i in range(len(a)-1):
        nextEnd = max(nextEnd, i + a[i])
        if currEnd == i:
            currEnd = nextEnd
            jump += 1
    return jump

L=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(jump(L))
#Output:
Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9] 
Output: 3 (1-> 3 -> 9 -> 9)
