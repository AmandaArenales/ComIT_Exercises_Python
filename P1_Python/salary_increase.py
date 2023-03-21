"""Make the program in Python such that given as a worker's salary, 
apply a 15% increase if your salary is less than $ 1000 and 12% otherwise. 
Print the new salary of the worker. """

salary = float(input("Please, insert your salary: "))

if salary < 1000:
    new_salary = (salary * (15/100)) + salary
    print(f"Your salary will be increased by 15% and your new salary is {new_salary}.")
else:
    new_salary = (salary * (12/100)) + salary
    print(f"Your salary will be increased by 12% and your new salary is {new_salary}.")

