"""Make a class called Person with the following conditions:
Its attributes are: name, age, id, gender (M male, F female), weight and height. 
We do not want direct access to them. Think which access modifier is the most appropriate, 
also its type. If you want to add some extra attribute you can do it. By default, all attributes 
except the Id will be default values ​​according to their type (0 for numbers, empty string for String, etc.). 
Gender will be male by default, use a constant for it. Several constructors will be implemented: 
A default constructor. A constructor with the name, age and gender, the rest by default. A constructor 
with all the attributes as parameters. The methods that will be implemented are: 
Calculate (): calculate if the person is at his ideal weight (weight in kg / (height ^ 2 in meters)), 
return -1 if he is below his ideal weight, 0 if he’s at his ideal weight and 1 if he’s overweight. 
Use constants to return these values. isOver18 (): indicates if it is of legal age, it returns a Boolean. 
CheckGender(char gen): Check if the entered gender is correct. It will not be visible outside the class. 
ToString (): returns all object information. GeneratesID (): generates a random number of 8 digits. 
This method will be invoked when the object is built. You can split the method to make it easier for you. 
It will not be visible outside the class. Setter of each attribute except ID. 
Now, create an executable class that does the following:
Ask by keyboard the name, age, gender, weight and height. Create 3 objects of the previous class. 
The first object will get the previous variables requested by keyboard, the second object will get all 
the previous ones but the weight and height by default, and the last one everything by default. 
For the latter, use setter methods to give values to the attributes. For each object, you should check 
if you are at ideal weight, overweight or below ideal weight and show a message. Indicate for each object 
if it is of legal age. Finally, display the information of each object. You can use methods in the 
executable class, to make it easier for you. Assume ideal BMI is 18.5 and 25 kg/m²""" 

import random
class Person: 
    name = " "
    age = 0
    __id = ""
    gender = "M"
    weight = 0.0
    height = 0.0
    
    def __init__(self, *args):
        if len(args) == 0:
            self.__id = self.__GeneratesID()
        elif (len(args) == 3):
            self.name = args[0]
            self.age = args[1]
            self.gender = args[2]
            self.__id = self.__GeneratesID()
        elif (len(args) == 6):
            self.name = args[0]
            self.age = args[1]
            self.gender = args[2]
            self.__id = args[3]
            self.weight = args[4]
            self.height = args[5]
   
    def set_name(self, name):
        self.name = name    
        
    def set_age(self, age):
        self.age = age
    
    def set_gender(self, gender):
        self.gender = gender

    def set_weight(self, weight):
        self.weight = weight 
    
    def set_height(self, height):
        self.height = height 
    
    def Calculate(self):
                      
        if (self.weight == 0.0) or (self.height == 0.0):
            print("Invalid weight or height.")
            return 
        
        bmi =  self.weight/(self.height ** 2)
        
        if bmi < 18.5:
            print(f"You are underweight. Your body mass index is: {bmi}.")
            return -1        
        elif 18.5 <= bmi <= 25:
            print(f"You are at the ideal weight. Your body mass index is: {bmi}.")
            return 0
        else:
            print(f"You are overweight. Your body mass index is: {bmi}.")
            return 1

    def isOver18(self):
        if self.age >= 18:
            print("You have a legal age.")
            return True 
        else:
            print("You don't have a legal age.") 
            return False
    
    def __CheckGender(self):
        if (self.gender == "M") or (self.gender == "F"):
            return True
        else:
            print("The entered gender is not correct, please insert M or F.")
        
    def __str__(self):
        return ("\nName: " + self.name +  "\nAge: " + str(self.age) + 
                "\nGender: " + self.gender +  "\nID: " + self.__id +
                "\nWeight: " + str(self.weight) + "\nHeight: " + str(self.height))

    #This is a private method. To define it I named the method with the double underscore "__"
    def __GeneratesID (self):
        return ''.join(["{}".format(random.randint(0, 9)) for num in range(8)])
    
print("Please, fill out the person information: \n")
name =  input("Please, insert the name: ")
age = int(input("Please, insert the age: "))
gender = input("Please, insert the gender((M - Male or F - Female)): ")
id = input("Please, insert the ID . It must have 8 digits ")
weight = float(input("Please, insert the weight in kg: "))
height = float(input("Please, insert the height in meters: "))
    
p1 = Person(name, age, gender, id, weight, height)
p2 = Person(name, age, gender)
p3 = Person()


print(f"\nThis are the information about BMI: \n")
p1.Calculate()
p2.Calculate()
p3.Calculate()

print(f"\nThis is the information about the age: \n")
p1.isOver18()
p2.isOver18()
p3.isOver18()

print(f"\nThis are the information of person: ")
print(p1)
print(p2)
print(p3)
