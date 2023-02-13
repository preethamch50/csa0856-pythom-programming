l=[1,2,3,1,1,3]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            print(("(i,j)"))
