# while loop with a condition
# reverse output
word = "palindromes"
index = len(word) - 1  # determine the index of the last character
while index >= 0:  # a condition is set
    letter = word[index]  # take one index
    print(letter)
    index = index - 1  # reduce the index
print()

# the best way with slices
# [::x] :-start, :-stop, x-step
nword = "murder"
rev = nword[::-1]  # redrum, -1 from the last index
print(rev)
two = nword[::2]  # mre, 2 through one index
print(two)
first = nword[:3]  # mur, take the first 3 letter
print(first)
last = nword[-3:]  # der, -3 count three char from the end, : go to the very end
print(last)
