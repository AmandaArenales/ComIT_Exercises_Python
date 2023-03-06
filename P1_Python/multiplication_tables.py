#Make a program that prints the 10 multiplication tables.

n = 1
m = 0

while n < 11:
    print(f"Multiplies of {n}")
    while m < 10:
        m = m + 1
        multiplier = m * n
        print (f"{n} x  {m} = {multiplier}")
    n = n + 1
    m = 0
    