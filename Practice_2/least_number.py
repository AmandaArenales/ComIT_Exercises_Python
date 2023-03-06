"""Write an algorithm to determine the least of a series of 
numbers that are read from the keyboard. The user ends by entering -1"""

def least_number():
    number = 0
    number  = float(input("Please, insert the first number: "))
    least = number
    list_numbers = []
    list_numbers.append(number)

    while number != -1:
        new_number  = float(input("Please, insert a number or -1 if you don't want to enter other number: "))

        number = new_number
        list_numbers.append(number)

    least = min(list_numbers)

    print (f"The least number in {list_numbers} is {least}")

least_number()