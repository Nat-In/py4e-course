# if statement
numb = int(input("Enter a number between 1 and 100: "))  # convert a string to a number
if numb > 50:
    print(numb, " is greater than 50")
if numb < 50:
    print(numb, " is less than 50")
if numb == 50:  # == is a comparison operator
    print(numb, " is exactly the middle")
print()

# alternative execution, in which there are two possibilities and the condition determines which one gets executed
add = int(input("Enter an additional positive number: "))
new_numb = numb + add
if new_numb % 2 == 0:  # % operator shows the remainder of a division
    print(new_numb, " is even")
else:
    print(new_numb, " is odd")
