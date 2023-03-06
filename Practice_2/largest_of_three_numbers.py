"""Create an algorithm to determine the largest of 3 numbers."""


def largest_of_three_numbers():
    number_1 = float(input("Please, insert the first number: "))
    number_2 = float(input("Please, insert the second number: "))
    number_3 = float(input("Please, insert the third number: "))

    if (number_1 > number_2) and (number_1 > number_3):
        largest = number_1
    elif (number_2 > number_1) and (number_2 > number_3):
        largest = number_2
    else:
        largest = number_3

    print (f"The largest number between {number_1}, {number_2} and {number_3} is {largest}")

largest_of_three_numbers()
