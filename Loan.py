p = float(input("Enter principal loan amount: "))
r = float(input("Enter monthly interest rate: "))
n = float(input("Enter total number of months: "))
m = p*(r*(1+r)**n) / ((1+r)**n-1)
print("The monthly payment is: ", m)