#Write an algorithm to print and count the multiples of 3 from 1 to 
#a number that we enter by keyboard

def count_mult_three():
	n = int(input("Please, insert a number: "))
	
	count = 0
	number = 0
	
	while number < n:
		number = number + 1
		if (number % 3) == 0:
			count = count + 1
	
	print(f"Between 1 and {n} we have {count} numbers that is multiplies of 3.")
			
count_mult_three()