#Write a Python function sumsquare(l) that takes a nonempty list of
#integers and returns a list [odd, even], where odd is the sum of squares
#of all the odd numbers in l and even is the sum of squares of all the even
#numbers in l.

def sumsquare(l):
    odd=[]
    even=[]
    l3=[]
    for i in range(0,len(l)):
        if l[i]%2!=0:
            odd.append(l[i])
        else:
            even.append(l[i])
    print(odd, even)
    oddsquare=sum([x**2 for x in odd])
    l3.append(oddsquare)
    evensquare=sum([y**2 for y in even])
    l3.append(evensquare)
    return l3
n=int(input("Enter the number of elements:"))
l1=[]
while True:
   
    num=int(input("Enter the element="))
    if num=="":
        break
    else:
        l1.append(num)
        if len(l1)==n:
            break
print(l1)

print(sumsquare(l1))

#output:
#Enter the number of elements:5
#Enter the element=1
#Enter the element=2
#Enter the element=3
#Enter the element=4
#Enter the element=5
#[1, 2, 3, 4, 5]
#[1, 3, 5] [2, 4]
#[35, 20]
