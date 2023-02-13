#You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Sol:
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
 
# Driver program
s = int(input("Enter the value of n: "))
print ("Number of ways = ", end="")
print (fib(s+1))

#Output:
Enter the value of n: 5
Number of ways = 8
