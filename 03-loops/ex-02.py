# infinite loop with while True. The condition is always true
# use when the exit condition is complex or depends on user/external data within the loop itself
# the loop will run forever until it forcibly terminated from within
import math  # import a non-build-in module

while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break  # loop exit point

    # handles errors, ValueError -the right type but an inappropriate value
    try:
        number = int(user_input)
        if number < 0:
            number = abs(number)  # abs() build-in function -takes number modulus
        square = math.isqrt(number)  # the module method is used through a dot
        print(f"The square root of a {number} is {square}.")
        continue

    except ValueError:
        print("Error! This is not a integer. Try again.")
        continue  # continue the cycle with new input
