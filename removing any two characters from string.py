str=input("enter any string ")
c=input("enter any two character ")
newtext=""
for i in range(len(str)):
    if str[i] not in c:
        newtext = newtext + str[i]
print("\nstring after removing character: ")
str =newtext
print(str)
    
