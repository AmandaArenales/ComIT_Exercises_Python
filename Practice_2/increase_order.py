"""Develop an algorithm to determine 
if a series of numbers that the user is entering is in increasing order or not"""

def increase_order():
    number = float(input("Please, insert a number: "))
    list_number = []
    list_number.append(number)

    while number != -1: 
        new_number = float(input("Please, insert a number or -1 if you don't want to enter other number: "))
        list_number.append(new_number)
        number = new_number
    
    list_number.pop()
    list_sort = list_number.copy()
    list_sort.sort()
 
    if list_number == list_sort:
        print(f"The series of numbers: {list_number} entered by the user is in increasing order.")
    else:
        print(f"The series of numbers: {list_number} entered by the user is not in increasing order.")

increase_order()