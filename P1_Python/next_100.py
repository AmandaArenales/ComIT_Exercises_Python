"""Write a program in Python that reads an integer from the keyboard 
and makes the sum of the next 100 numbers, showing the result on screen."""

n = int(input("Please, insert a integer number: "))

count = 1

while count < 100:
    count = count + 1
    sum = n + count
print (f"The sum of {n} and the next 100 numbers is: {sum}") 