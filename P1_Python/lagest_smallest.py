"""Write a program in Python that 
reads two numbers on the keyboard and say which is the largest and which is the smallest."""

x = int(input("Please, insert a number: "))
y = int(input("Please, insert a number: "))

if x > y:
    print(f'Number {x} is the largest number!')
    print(f'Number {y} is the smallest number!')
elif y > x:
    print(f'Number {y} is the largest number!')
    print(f'Number {x} is the smallest number!')
else:
    print(f'Number {x} is the equal number {y}!')