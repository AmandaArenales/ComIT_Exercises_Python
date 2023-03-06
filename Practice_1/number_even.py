#Write an algorithm that determines if a number is even.

def number_even():
    n = int(input("Please, insert a number: "))
	
    if n % 2 == 0:
        print (f"The number {n} is an even number!")
    else:
        print (f"The number {n} is not an even number!")

number_even()
