"""Create an algorithm to determine the largest of a series of 
numbers that are read from the keyboard. The user ends by entering -1."""

def largest_number():
    number = 0
    number  = float(input("Please, insert the first number: "))
    largest = number
    list_numbers = []
    list_numbers.append(number)

    while number != -1:
        new_number  = float(input("Please, insert a number or -1 if you don't want yo enter other number: "))
        
        if (new_number > largest):
            largest = new_number
        
        number = new_number
        list_numbers.append(number)

    print (f"The largest number in {list_numbers} is {largest}")

largest_number()