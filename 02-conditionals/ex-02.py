# A program for calculating gross pay
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours
# Catching an exception with a try/except statement
# Catching an exception gives a chance to fix the problem, or try again, or end the program gracefully
user_hours = input("Enter Hours: ")
user_rate = input("Enter Rate: ")
try:
    fhour = float(user_hours)
    frate = float(user_rate)
except:
    print("Error, pleas enter numeric input")
    quit()  # sys.exit() -in real projects / quit() -training version
# print(fhour,frate)

if fhour > 40:
    reg = fhour * frate  # type: ignore
    ovt = (fhour - 40.0) * (frate * 0.5)  # calculate the overtime hours
    print("Your supplement is: ", ovt)
    pay = reg + ovt
else:
    pay = fhour * frate  # type: ignore
print("Your pay is: ", pay)
