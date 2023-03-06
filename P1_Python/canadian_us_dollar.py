"""Write a program in Python that converts from canadian 
dollars to US dollars. You will receive a decimal number corresponding 
to the amount in CAD and will answer with the corresponding amount in US dollars. 
Take the quotation of the dollar today.
"""

canadian_dollar = float(input("Please, insert the amount of canadian dollar to convert: "))
quotation = float(input("Please, insert quotation of the dollar today: "))

amount_usa = float(canadian_dollar * quotation)

print (f"The amount of CAD${canadian_dollar} is equivalent of US${amount_usa}.")