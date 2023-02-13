n=int(input("Enter  value of n"))
p=[]
for i in range(1,n+1):
    if(i%3==0):
        p.append("fizz")
    elif(i%5==0):
        p.append("buzz")
    elif(i%3==0 and i%5==0):
        p.append("fizzbuzz")
    else:
        p.append(str(i))
print(p)
