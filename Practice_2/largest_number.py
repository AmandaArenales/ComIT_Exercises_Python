"""Create an algorithm to determine the largest of a series of 
numbers that are read from the keyboard. The user ends by entering -1."""

def largest_number():
    number = 0
    number  = float(input("Please, insert the first number: "))
    list_numbers = []
    list_numbers.append(number)

    
    while number != -1:
        new_number  = float(input("Please, insert a number or -1 if you don't want yo enter other number: "))
        
        for n in list_numbers:
            if (new_number > number):
                largest = new_number
        
        number = new_number
        list_numbers.append(number)

    print (f"The largest number between {list_numbers} is {largest}")

largest_number()