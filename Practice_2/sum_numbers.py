"""Write an algorithm that reads a series of real numbers and 
adds them, printing the result. The series ends when the user enters the number zero."""

def sum_number():
    r_numbers = 0
    sum_numbers = 0
    count = 0 
    r_numbers = float(input("Please, insert a number: "))
    sum_numbers = r_numbers

    while r_numbers != 0:
        r_numbers = float(input("Please, insert a number or insert 0 if you want to stop: "))
        sum_numbers = r_numbers + sum_numbers 
        count = count + 1
    print (f"You insert {count} and their sum {sum_numbers}") 
sum_number()