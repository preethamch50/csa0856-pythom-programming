#The Project manager has to submit the project within a week period. He didn’t find the proper combinations of team members to work on the project, Help him in finding the possible combinations available. 
Accept 3 digits and find all the combinations

Program:
import itertools 
digit=3
num=input("Enter the number:")

while True:
    x=True
    if (len(num)!=digit):
        x=False
        print("Invalid Input, OUT OF LIMIT!")
    elif digit==2:
        if num[0]==num[1]:
            print("Invalid input, unique permutation")
            x=False
    elif digit==3:
        if (num[0]==num[1]==num[2]):
            print("Invalid input, unique permutation")
            x=False
    break
if x==True:
    nums=list(num)
    permutations = list(itertools.permutations(nums))
    p=([''.join(permutation) for permutation in permutations])
print(*p)
Output:
Sample Input: 
123 
Sample Output: 
123 
132 
213 
231 
312 
321
