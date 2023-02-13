#In an organization they decide to give bonus to all the employees on New Year. A 5% bonus on salary is given to the grade A workers and 10% bonus on salary to the grade B workers. Write a program to enter the salary and grade of the employee. If the salary of the employee is less than $10,000 then the employee gets an extra 2% bonus on salary Calculate the bonus that has to be given to the employee and print the salary that the employee will get.

Sol:
#Employee bonus program
Grade=input("Enter the Grade: ")
sal=eval(input("Enter the Salary: "))
Bonus=0
total_sal=0
while sal>0:
    if sal<=10000:
        Bonus=sal*(2/100)
        total_sal=sal+Bonus
        print("Bonus=",Bonus)
        print("Total salary",total_sal)
        break
    elif(Grade=='A' and sal>10000):
        Bonus=sal*(5/100)
        total_sal=sal+Bonus
        print("Bonus=",Bonus)
        print("Total salary",total_sal)
        break
    else:
        Bonus=sal*(10/100)
        total_sal=sal+Bonus
        print("Bonus=",Bonus)
        print("Total salary",total_sal)
        break

Output:
Enter the Grade: B
Enter the Salary: 50000
Bonus= 5000.0
Total salary 55000.0
3.	
