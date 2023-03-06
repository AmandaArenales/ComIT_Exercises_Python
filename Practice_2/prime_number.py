"""Write an algorithm to determine if a number read by keyboard is prime."""

def prime_number():
    number = int(input("Please, insert a number: "))
    isprime = True

    for i in range(2, number):
        if (number % i) == 0:
            isprime = False
            break
    
    if isprime:
        print(f"The number {number} is prime.")
    else:
        print(f"The number {number} is not prime.")

prime_number()