#Implement a triangular array of the binomial coefficients that arises in probability theory, combinatorics, and algebra. Find the sum of elements in the nth row.
Sol:
# input n  
n = int(input("Enter the number of rows:"))  
  
# iterarte upto n  
for i in range(n):  
   # adjust space  
   print(' '*(n-i), end='')  
  
   # compute power of 11  
   print(' '.join(map(str, str(11**i))))

sum=0
row=int(input("Enter the row number: "))
sum = sum + (1 << row)
print(sum)

# Sum of all elements
sum=0
for row in range(n):
   sum = sum + (1 << row)
print(sum)

Output:
Enter the number of rows:5
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
Enter the row number: 4
