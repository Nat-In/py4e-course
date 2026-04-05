# repeatedly prompt for numbers until the user enters "done"
# after "done", output the maximum and minimum values
# handle errors for non-integer inputs and skip to the next number
# before comparing ival with largest or smallest, check if they are None
# assign the value of ival to largest and smallest
# ensure comparison is only with numbers, not with None
largest = None  # None is universal for any data set
smallest = None
while True:
    sval = input("Enter the number: ")
    if sval == "done":
        break
    try:
        ival = int(sval)
    except:
        print("Invalid input")
        continue

    # if it's the first number, assign it
    # else, check if it's greater than the current max
    if largest is None:
        largest = ival
    elif ival > largest:
        largest = ival

    if smallest is None:
        smallest = ival
    elif ival < smallest:
        smallest = ival

print("Maximum is ", largest)
print("Minimum is ", smallest)
