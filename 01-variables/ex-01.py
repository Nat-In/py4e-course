# check the type of a variable using type()
number = 52
print(number, type(number))  # <class 'int'>

decimal = 3.14
print(decimal, type(decimal))  # <class 'float'>
integer = int(decimal)
print(integer, type(integer))  # <class 'int'>

string = "Word"
print(string, type(string))  # <class 'str'>

user_input = input("Enter your age number: ")
print(user_input, type(user_input))  # input() is always <class 'str'>
print("Is type of user input a digit?", type(user_input) == int)  # False

convert_input = int(user_input)
print(convert_input, type(convert_input))  # <class 'int'>
