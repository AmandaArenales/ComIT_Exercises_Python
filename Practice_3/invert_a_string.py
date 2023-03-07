"""Write an algorithm to invert a string of characters."""

string = input("Please, insert a string: ")
invert_string = ""

for letter in string:
    invert_string = letter + invert_string

print(f"The inverse of {string} is {invert_string}!")

#Or
invert_string = ""

for letter in range(1, len(string) + 1):
    invert_string = invert_string + string[-1 * letter]

print(f"The inverse of {string} is {invert_string}!")
    