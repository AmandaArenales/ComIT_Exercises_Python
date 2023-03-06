"""Perform an algorithm to read a number and report if it is greater, equal or less than zero"""

def compare_with_0():
    number = float(input("Please, insert a number: "))
	
    if number > 0:
	    print (f"The number {number} is greater than zero!")
    elif number == 0:
         print(f"The number {number} is equal zero!")
    else:
	     print (f"The number {number} is less than zero!")

compare_with_0()
