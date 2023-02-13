#Little Robert likes mathematics. Today his teacher has given him two integers and asked him to find out how many integers can divide both the numbers. Would you like to help him in completing his school assignment? For each test case, print “YEAH” if „prod‟ is divisible by „sum‟, otherwise print “NAH”.
Sol:
num1=int(input("Enter the number1: "))
num2=int(input("Enter the number2: "))

x=min(num1,num2)
l=[]
for i in range(1,x+1):
    if num1%i==0 and num2%i==0:
        l.append(i)
print(l, "\nNo. of intergers: ",len(l))

if(num1*num2)%(num1+num2)==0:
    print("YEAH")
else:
    print("NAH")

output:
Enter the number1: 10
Enter the number2: 15
[1, 5] 
No. of intergers:  2
YEAH
