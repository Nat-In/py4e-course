# use input in variables to promt a user for their name and then welcomes them
# \n at the end of the prompt represents a newline
name = input("What is your name?\n")
print("Hello", name)
# ask for hours and rate per hour to compute gross pay
xhour = input("Enter Hours: ")
xrate = input("Enter Rate: ")
# use float() to convert the string to a number
xpay = float(xhour) * float(xrate)
# roundet the result, left one simbol after coma
result = round(xpay, 1)
print("Pay:", result)
# add the premium to the pay
prem = 10
premium = result + 10
print("Your pay with bonus is: ", premium)

