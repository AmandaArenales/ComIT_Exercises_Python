"""Given a series of real numbers that are being read from the keyboard, 
determine the maximum value and the position of it."""

def largest_number():
    number = 0
    number  = float(input("Please, insert the first number: "))
    largest = number
    list_numbers = []
    list_numbers.append(number)

    while number != -1:
        new_number  = float(input("Please, insert a number or -1 if you don't want to enter other number: "))
      
        number = new_number
        list_numbers.append(number)
    
    largest = max(list_numbers)
    position = list_numbers.index(largest)

    print (f"The largest number in {list_numbers} is {largest} and the position of it is {position}.")

largest_number()