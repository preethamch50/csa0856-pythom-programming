#A bakery sells loaves of bread for 185 rupees each. Day old bread is discounted by 60
#percent. Write a program that begins by reading the number of loaves of day old bread being purchased from the user. Then your program should display the regular price for the bread, the discount because it is a day old, and the total price. All of the values should be displayed using two decimal places, and the decimal points in all of the numbers should be aligned when reasonable values are entered by the user.

Sol:
price=eval(input("Enter the regular price="))
fresh=int(input("Enter the no/- of fresh loaves purchased="))
old=int(input("Enter the no/- of old loaves purchased="))
fresh_amt=fresh*price
old_amt=old*(price*(40/100))
total=fresh_amt+old_amt
print("Regular price= %.2f" % price)
print("Amount for new loaves= %.2f" % fresh_amt)
print("Amount for old loaves= %.2f" % old_amt)
print("Total price= %.2f" % total)

#Output:
#Enter the regular price=185
#Enter the no/- of fresh loaves purchased=5
#Enter the no/- of old loaves purchased=3
#Regular price= 185.00
#Amount for new loaves= 925.00
#Amount for old loaves= 222.00
#Total price= 1147.00
