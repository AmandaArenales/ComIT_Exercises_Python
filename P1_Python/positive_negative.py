"""Write a Python program that declares an integer variable B 
and assign it a value. It then displays a message indicating 
whether the value of B is positive or negative. We will consider 0 as positive."""

B = int(input("Please, insert a number: "))

if B >= 0:
    print(f"The number {B} is positive!")
else:
   print(f"The number {B} is negative!") 