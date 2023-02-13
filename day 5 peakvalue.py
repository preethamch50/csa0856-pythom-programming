#A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array nums, find a peak element, and return its index.
Sol:
n=int(input("Enter the number of elements: "))
L=[]
while True:
    if len(L)==n:
        break
    else:
        num=input("Enter the element: ")
        L.append(num)
print(L)
max_val=max(L)
index_val=L.index(max_val)
print("Index of peak value: ", index_val)

output:
Enter the number of elements: 5
Enter the element: 1
Enter the element: 4
Enter the element: 2
Enter the element: 6
Enter the element: 3
['1', '4', '2', '6', '3']
Index of peak value:  3
