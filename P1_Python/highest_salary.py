"""Make a program that asks for the salary of N workers 
(first you must ask how many workers there are) and print the one with the highest salary."""

workers = int(input("Please, insert how many workers work in the company: "))
n = 0
salary_highest = 0

while n < workers:
    n = n + 1
    salary = float(input(f"Please insert the salary of worker {n}: "))
    
    if salary > salary_highest:
        salary_highest = salary
print(f"The highest salary of {workers} are {salary_highest}." )


