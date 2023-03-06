#Make an algorithm to read two real numbers and print the largest of them.

def compare_two_number():
	x  = int(input("Please, insert the first number: "))
	y  = int(input("Please, insert the second number: "))

	if x >  y:
	    print (f"The number {x} is greater than number {y}!")
	elif x == y:
         print(f"The number {x} equal number {y}!")
	else:
	     print (f"The number {x} is less than number {y}!")
	     
compare_two_number()


