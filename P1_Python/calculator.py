#Make a calculator.

number_1 = (input("Please, insert the first number: "))
operator = (input("Please, insert the operator: "))
number_2 = (input("Please, insert the second number: "))

calculator = eval(number_1 + operator + number_2)

print(f"The result of the expression is: {calculator}.")

