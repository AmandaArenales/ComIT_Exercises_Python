"""Create a class called Password with the following conditions:
It has the length and password attributes. By default, the length will be 8. 
The constructors will be as follows: A default constructor. A constructor with the length 
that we send as parameter. 


Generate a random password with that length. The methods you 
implement will be: isStrong (): return a boolean if it is strong or not, to be strong you 
must have more than 2 uppercase, more than 1 lower case and more than 5 numbers. 

GeneratePassword (): Generates the password of the object with the defined length. Get method for 
password and length. 

Set method for length. 

Now let’s create an executable class: Create an 
array of Passwords with the size that you indicate by keyboard. Create a loop that creates an
object for each position in the array. It also indicates by keyboard the length of the 
Passwords (before loop). Create another array of booleans where we store if the password of the 
password array is strong or not (use the previous loop). At the end, we show the password and 
whether or not it is strong (use the previous loop). Use this simple format: password1 boolean_value1
password2 boolean_value2"""

import random
import string

class Password:
    lenght = 8
    password = ""

    def __init__(self, *args):
        if (len(args) == 1):
            self.lenght = args[0]
        self.password = self.GeneratePassword()

    def isStrong (self): 
        uppercase = 0
        lowercase = 0
        number = 0

        if len(self.password) >= 8:
            for i in (self.password):
                if i.isupper():
                    uppercase += 1
                elif i.islower():
                    lowercase += 1
                elif i.isnumeric():
                    number += 1

            if (uppercase >= 2) and (lowercase >= 1) and (number >= 5): 
                return True
            else:
                return False
        else:
            return False

    def GeneratePassword (self):
        upper = list(string.ascii_uppercase)
        lower = list(string.ascii_lowercase)
        number = [ "{}".format(i) for i in range(0, 10)]
        [upper.extend(l) for l in (lower, number)]
    
        self.password = ''.join(["{}".format(random.choice(upper)) for _ in range(self.lenght)])
        return self.password

    def get_password(self):
        return self.password
    
    def set_length(self, lenght):
        self.lenght = lenght

    def get_length(self):
        return self.lenght
    
number_passwords = int(input("Please, insert how many passwords you want: "))
password_lenght = int(input("Please, insert the lenght of the password: "))

dictionary = {}

for i in range(number_passwords):
    p = Password(password_lenght)
    password = p.get_password()
    strong = p.isStrong()
    dictionary[password] = strong

for k,v in dictionary.items():
    print (f"Password: {k} -- boolean_value: {v}.")

