""" Write an algorithm that calls another name "add", which receives 2 numbers. 
The summation algorithm must add its parameters. The algorithm you invoke 
must receive that value and display it on the screen."""

def add(n_1, n_2):
    sum = n_1 + n_2
    print(f"The value generate by algorithm add is: {sum}!")


def algorithm_sum(n_1, n_2): 
    add(n_1, n_2)
number_1 = int(input("Please, insert the first number: "))
number_2 = int(input("Please, insert the second number: "))

algorithm_sum(number_1, number_2)