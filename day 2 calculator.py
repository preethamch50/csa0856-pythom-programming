#Basic Calculator II. Given a string s which represents an expression, evaluate this expression and return its value. The integer division should truncate toward zero.
Sol:
def calculate(s: str) -> int:
    s = s.replace(" ", "")
    s += '+'
    st = []
    num = 0
    op = '+'
    print(s)
    
    # num = ''
    for i in s:
        if i.isdigit():
            num = (num*10)+int(i)
            # num += i
        else:
            num = int(num)
            if op == '+':
                st.append(num)
            elif op == '-':
                st.append(-num)
            elif op == '*':
                st.append(st.pop()*num)
            elif op == '/':
                st.append(int(st.pop()/num))
            # num = ''
            num = 0
            op = i
            print(st)
    return sum(st)

exp=input("Enter the Expression:")
print(calculate(exp))

#Output:
Enter the Expression:3+4/2*5
13
