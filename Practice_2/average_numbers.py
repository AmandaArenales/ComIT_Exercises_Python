"""Write an algorithm to find the average of a series of numbers that 
are read from the keyboard."""

def average_numbers():
    r_numbers = 0
    count = 1
    sum_numbers = 0
    r_numbers = float(input("Please, insert a number: "))
    sum_numbers = r_numbers

    while r_numbers != 0:
        r_numbers = float(input("Please, insert a number or insert 0 if you want to stop: "))
        count = count + 1
        sum_numbers = r_numbers + sum_numbers 
    count = count - 1
    avg_numbers = (sum_numbers)/ count
    print (f"You insert {count} and their sum {avg_numbers}") 
average_numbers()