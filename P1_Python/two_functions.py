#Write an algorithm that calls another, and the call prints a value.

def print_number():
    number = int(input("Please, insert a number: "))
    print(f"The number {number} will be print because the function algorithm_1!")


def algorithm_1(): 
    print_number()

algorithm_1()