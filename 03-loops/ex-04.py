"""for loop -is used to repeat a block of code for every item in a sequence(list,string,range)"""

# repiat counting
word = "apple"
count = 0
for char in word:
    if char == "p":
        count += 1
print(count)

# filter
text = "a1b2c3"
result = ""
for char in text:
    # .isdigit() -returns True if the character is a digit, False otherwise
    # not -logical operator that flips the result. If char.isdigit() is True 'not' makes it False(skip)
    if not char.isdigit():
        result += char
print(result)

# count vowels
clause = "Anything you want"
vowels = "aeiouAEIOU"
count = 0
for char in clause:
    if char in vowels:
        count += 1
print(count, "Vowels")

# find the longest & shortest word
words = ["cat", "elephant", "dog", "iguana", "platypus"]
longest = []
shortest = []
max_length = 0
min_length = None  # because len(word) > 0 is always True
for word in words:
    # find the longest word
    if len(word) > max_length:
        max_length = len(word)
        longest = [word]  # replace the list with a new one
    elif len(word) == max_length:
        longest.append(word)  # adding words of the same length as the longest one

    # find the shortest word
    if min_length is None:  # initiate the first entry
        min_length = len(word)
        shortest = [word]
    elif len(word) < min_length:
        shortest = [word]  # replace the list
    elif len(word) == min_length:
        shortest.append(word)

print(longest)
print(shortest)
