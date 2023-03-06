#Write an algorithm that determines if an "N" number is divisible by another "M".

def number_divisible(): 
    n = int(input("Please, insert the first number: "))
    m  = int(input("Please, insert the second number: "))

    if n % m == 0:
	    print (f"{n} number is divisible by {m} number")
    else:
        print (f"{n} number is not divisible by {m}")

number_divisible()