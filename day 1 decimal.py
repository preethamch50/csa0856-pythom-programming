#A valid number can be split up into these components (in order):
#1. A decimal number or an integer.
#2. (Optional) An 'e' or 'E', followed by an integer.
def isNumber(s):
    valid_patterns = ('xd','x.d','xd.','xd.d','xsd','xsd.',
              'xsd.d','xded','x.ded','xd.ed','xd.ded',
              'xsded','xsd.ed','xsd.ded', 'xdesd', 'x.desd', 
              'xd.esd', 'xd.desd', 'xsdesd', 'xsd.esd', 
              'xsd.desd', 'xs.d', 'xs.ded', 'xs.desd'
              )
    patttern = 'x'
    for ch in s:
        if ch == '+' or ch == '-': patttern += 's'
        elif ch == 'e' or ch == 'E': patttern += 'e'
        elif ch.isdigit():
            if patttern[-1] != 'd': patttern += 'd'
        elif ch == '.': patttern += '.'
        else: return False
        
    return patttern in valid_patterns
str1=input("String=")
print(isNumber(str1))

#output:
#String=2.90
#True
