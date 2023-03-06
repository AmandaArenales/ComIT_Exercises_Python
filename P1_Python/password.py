""" Write a program that asks for a numerical password and allows 
three attempts. If the user enters the correct password, it shows "Correct!" 
And run any program, after the message. Otherwise the program 
should display "Wrong password". Then finish the program immediately."""

password = "passwordcomIT2023"
attempts = 0

while attempts < 3:
    attempts = attempts + 1
    user_password = input("Please, insert the password: ")
    if user_password == password:
        print("Your password is correct. You will acess the program soon. ")
        break
    elif attempts == 3: 
        print("Sorry, your password is wrong again. Did you forget your password?")
    else:
        print("Your password is incorrect, try it again!")



