"""Make a class called Person with the following conditions: Its attributes are: name, age, id, 
gender (M male, F female), weight and height. We do not want direct access to them. Think which 
access modifier is the most appropriate, also its type. If you want to add some extra attribute 
you can do it. By default, all attributes except the Id will be default values ​​according to their
type (0 for numbers, empty string for String, etc.). Gender will be male by default, use a constant 
for it. Several constructors will be implemented: A default constructor. A constructor with the name, 
age and gender, the rest by default. A constructor with all the attributes as parameters. The methods 
that will be implemented are: Calculate (): calculate if the person is at his ideal weight 
(weight in kg / (height ^ 2 in meters)), return -1 if he is below his ideal weight, 0 if he’s at his 
ideal weight and 1 if he’s overweight. Use constants to return these values. isOver18 (): indicates if
 it is of legal age, it returns a Boolean. CheckGender(char gen): Check if the entered gender is correct. 
 It will not be visible outside the class. ToString (): returns all object information. GeneratesID (): generates 
 a random number of 8 digits. This method will be invoked when the object is built. You can split the method 
 to make it easier for you. It will not be visible outside the class. Setter of each attribute except ID. 
Now, create an executable class that does the following: Ask by keyboard the name, age, gender, weight and height.
Create 3 objects of the previous class. The first object will get the previous variables requested by keyboard, 
the second object will get all the previous ones but the weight and height by default, and the last one everything 
by default. For the latter, use setter methods to give values to the attributes. For each object, you should check 
if you are at ideal weight, overweight or below ideal weight and show a message. Indicate for each object if 
it is of legal age. Finally, display the information of each object. You can use methods in the executable class, 
to make it easier for you."""