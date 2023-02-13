#Write a function shuffle(l1,l2) that takes as input two lists, 11 and l2, and returns a list consisting of the first element in l1, then the first element in l2, then the second element in l2, then the second element in l2, and so on. If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.
Sol:
def shuffle(l1,l2):
    new_list=[]
    n=len(l1)
    m=len(l2)
    x=min(n,m)
        
    for i in range(x):
        new_list.append(l1[i])
        new_list.append(l2[i])
        
    if len(l1)!=len(l2):
        if(n>m):
            new_list.append(l1[x:])
        elif (m>n):
            new_list.append(l2[x:])
    return new_list
            
#Driver Program
list1=[1,3,5]
list2=[2,4,6,8,10]
y=shuffle(list1,list2)
print(*y)

Output:
[1, 2, 3, 4, 5, 6, [8, 10]]
