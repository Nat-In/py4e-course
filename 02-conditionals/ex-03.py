# chained conditional whit if/elif
# when there are more than two possibilities and we need more than two branches
# a program to prompt for a score between 0.0 and 1.0
# if the user enters a value out of range, print a suitable error message and exit
score = input("Enter score between 0.0 and 1.0: ")
try:
    fscr = float(score)
    if (
        fscr < 0 or fscr > 1
    ):  # logical OR returns True if at least one of the conditions is true
        print("Bad score")
    elif fscr >= 0.9:
        print("A")
    elif fscr >= 0.8:
        print("B")
    elif fscr >= 0.7:
        print("C")
    elif fscr >= 0.6:
        print("D")
    else:
        fscr < 0.6
        print("F")
except:
    print("Incorrect input. Please try again.")
    quit()
