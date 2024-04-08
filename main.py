"""
PowerOfTen
"""
# Provide your solution here
number=int(input("Please enter a max. 3-digit-number: "))
if number <=0:
    print(f"The number cannot be negative.")
elif number > 999:
    print(f"The number cannot have more than 3 digits.")
else:
    print(f"{number} = {number//10}*10 + {number%10}")
"""
Cash Box
"""
# Provide your solution here
pay=int(input("Please enter the amount to be paid: "))
rec=int
if pay <=0:
    print(f"Negative payment is invalid.")
    pay=int(input("Please enter the amount to be paid: "))
else:
    rec=int(input("Please enter the amount received: "))
    if rec <=0:
        print(f"Negative received amount is invalid.")
        rec=int(input("Please enter the amount received: "))
if pay <= rec:
    print(f"Your change is {rec-pay} €.")
elif pay >= rec:
    print(f"You did not pay enough.")
    pay = int(input("Please enter the amount to be paid: "))
    rec = int(input("Please enter the amount received: "))




