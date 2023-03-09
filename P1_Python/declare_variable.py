"""Write a Python program that does the following: 
declare a variable N of type int, a variable A of type double and a 
variable C of type char and assign to each one a value. The following screen displays:
The value of each variable. The sum of N + A. And A - N"""

N: int = 2
A: float = 3.3
C: chr = A

print(f'The value of N is: {N}\n')
print(f'The value of A is: {A}\n')
print(f'The value of C is: {C}\n')

print(f"The sum of {N} + {A} is {N + A}.\n")

print(f"The substraction of {A} - {N} is {N - A}.\n")
