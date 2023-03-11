# ComIT_Exercises_Python

In this repository you will find several exercises solution in Python code. 

## P1_Python

1. Python fundamentals. It has 14 exercises: [`print_examples.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P1_Python/print_examples.py)

1. Exercise: Write a program in Python that prints the squares of the first 30 natural numbers on the screen: [`square_30.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P1_Python/square_30.py)

1. Write a program in Python that reads an integer from the keyboard and makes the sum of the next 100 numbers, showing the result on screen: [`next_100.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P1_Python/next_100.py)

1. Write a program in Python that converts from canadian dollars to US dollars. You will receive a decimal number corresponding 
to the amount in CAD and will answer with the corresponding amount in US dollars. 
Take the quotation of the dollar today: [`canadian_us_dollar.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P1_Python/canadian_us_dollar.py)

1. Write a program in Python that reads two numbers on the keyboard and say which is the largest and which is the smallest: [`lagest_smallest.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P1_Python/lagest_smallest.py)

1. Write a Python program that does the following: declare a variable N of type int, a variable A of type double and a variable C of type char and assign to each one a value. The following screen displays: The value of each variable. The sum of N + A. And A - N: [``]()
 
1. Write a Python program that declares an integer variable B and assign it a value. It then displays a message indicating whether the value of B is positive or negative. We will consider 0 as positive: [`positive_negative.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P1_Python/positive_negative.py)

1. Make a program in Python such that given as data the enrolment and 5 grades of a student; Print the enrolment, the average and the word "approved" if the student has an average greater than or equal to 6, and the word "not approved" otherwise. Data: MAT, CAL1, CAL2, CAL3, CAL4, CAL5 Where: MAT is an integer variable that represents the student's enrolment. CAL1, CAL2, CAL3, CAL4 and CAL5 are real-type variables representing the student's 5 grades: [`grades.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P1_Python/grades.py)

1. Make the program in Python such that given as a worker's salary, apply a 15% increase if your salary is less than $ 1000 and 12% otherwise. Print the new salary of the worker. Fact: SUE (variable of real type that represents the salary of the worker): [`salary_increase.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P1_Python/salary_increase.py)

1. Make a program that prints the 10 multiplication tables: [`multiplication_tables.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P1_Python/multiplication_tables.py)

1. Make a calculator: [`calculator.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P1_Python/calculator.py)

1. Calculate the salary increase for a group of employees of a company considering the following criteria: If the salary is less than $ 1,000.00: Increase 15% If the salary is greater than or equal to $ 1,000.00: Increase 12% The program must do The following: - Save the new salaries in the arrangement - Calculate the payroll - Print the salaries from the settlement: [``]()

1. Make a program that asks for the salary of N workers (first you must ask how many workers there are) and print the one with the highest salary: [`highest_salary.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P1_Python/highest_salary.py)

1. Write a program that asks for a numerical password and allows three attempts. If the user enters the correct password, it shows "Correct!" And run any program, after the message. Otherwise the program should display "Wrong password". Then finish the program immediately: [`password.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P1_Python/password.py)

## P2_Python

1. Write an algorithm that calls another, and the call prints a value: [`two_functions.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P2_Python/two_functions.py)

1. Write an algorithm that calls another name "add", which receives 2 numbers. The summation algorithm must add its parameters. The algorithm you invoke must receive that value and display it on the screen: [`two_algorithm_sum.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P2_Python/two_algorithm_sum.py)

1. Write an algorithm and a sub-algorithm. Write two variables with the same name and the compiler does not show error: [`equal_variables.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P2_Python/equal_variables.py)

## P3_Python

1. Write a program that allows you to enter the height of 10 students, then show the average height, and how many elements are above average, how many are below average: [`height.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P3_Python/height.py)

1.  Write an algorithm (Vehicles.py) that, from reading and storing in vectors the commercial 
value of 20 vehicles and the type (family (1), public transportation (2), load (3)), calculate the new
value: [`vehicles.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P3_Python/vehicles.py)

1. A survey was carried out to 15 students in a University where the following information was requested: Photo ID #, Sex, Salary, Job: [`poll.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P3_Python/poll.py)

## P4_Python

1. Create a class called Book that stores the information for each of the books in a library. The class should keep the title of the book, author, number of copies of the book and number of lend copies. The class will contain the following methods: Default constructor. Constructor with parameters. 
Setters / getters. Method Loan that increases the corresponding attribute each time a loan is made from the book. No books may be borrowed if no copies are available to lend. Returns true if the operation was successful and false otherwise.  Returns method that decrements the corresponding attribute
when a book is returned. No books can be returned that have not been lend. Returns true if the operation was successful and false otherwise. ToString method to display data from books. This method is inherited from Object and we must modify it (override) to adapt it to the Book class. 
Write a program to test the operation of the Book class: [`books.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P4_Python/books.py)

1. Make a class called Person with the following conditions: Its attributes are: name, age, id, gender (M male, F female), weight and height. We do not want direct access to them. Think which access modifier is the most appropriate, also its type. If you want to add some extra attribute you can do it. By default, all attributes except the Id will be default values according to their type (0 for numbers, empty string for String, etc.). Gender will be male by default, use a constant for it. Several constructors will be implemented: A default constructor. A constructor with the name, age and gender, the rest by default. A constructor with all the attributes as parameters. The methods that will be implemented are: Calculate (): calculate if the person is at his ideal weight (weight in kg / (height ^ 2 in meters)), return -1 if he is below his ideal weight, 0 if he’s at his ideal weight and 1 if he’s overweight. Use constants to return these values. isOver18 (): indicates if it is of legal age, it returns a Boolean. CheckGender(char gen): Check if the entered gender is correct. It will not be visible outside the class. ToString (): returns all object information. GeneratesID (): generates a random number of 8 digits. This method will be invoked when the object is built. You can split the method to make it easier for you. It will not be visible outside the class. Setter of each attribute except ID. Now, create an executable class that does the following: Ask by keyboard the name, age, gender, weight and height. Create 3 objects of the previous class. The first object will get the previous variables requested by keyboard, the second object will get all the previous ones but the weight and height by default, and the last one everything by default. For the latter, use setter methods to give values to the attributes. For each object, you should check if you are at ideal weight, overweight or below ideal weight and show a message. Indicate for each object if it is of legal age. Finally, display the information of each object. You can use methods in the executable class, to make it easier for you. Assume ideal BMI is 18.5 and 25 kg/m²: [`person.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/P4_Python/person.py)

## Practice_1

1. Perform an algorithm to read a number and report if it is greater, equal or less than zero: [`compare_with_zero.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_1/compare_with_zero.py)

1. Write an algorithm that determines if a number is even: [`number_even.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_1/number_even.py)

1. Make an algorithm to read two real numbers and print the largest of them:: [`compare_two_numbers.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_1/compare_two_numbers.py)

1. Given the radius of a circle, make an algorithm to calculate the value of the area: [`area_circle.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_1/area_circle.py)

1. Write an algorithm that determines if an "N" number is divisible by another "M": : [`divisible_numbers.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_1/divisible_numbers.py)

1. Write an algorithm to translate a time expressed in days, hours, minutes and seconds to time expressed in 
seconds: [`days_to_seconds.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_1/days_to_seconds.py)

1. We are being informed of three environmental temperature values, and we are asked to develop an algorithm to 
calculate and report the sum and average of these values: [`temperature_sum_avg.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_1/temperature_sum_avg.py)

1. Translate a time expressed in seconds to a time expressed in days, hours, minutes and 
seconds: [`seconds_to_days.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_1/seconds_to_days.py)

## Practice_2

1. Create an algorithm to determine the largest of 3 numbers: [`largest_of_three_numbers.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_2/largest_of_three_numbers.py)

1. Create an algorithm to determine the largest of a series of numbers that are read from the keyboard. The user 
ends by entering -1: [`largest_number.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_2/largest_number.py)

1. Write an algorithm to determine the least of a series of numbers that are read from the keyboard. The user ends 
by entering -1: [`least_number.p`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_2/least_number.py)

1. Write an algorithm to print and count the multiples of 3 from 1 to a number that we enter by keyboard: [`multiplies_of_three.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_2/multiplies_of_three.py)

1. Write an algorithm that reads a series of real numbers and adds them, printing the result. The series ends when 
the user enters the number zero: [`sum_numbers.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_2/sum_numbers.py)

1. Write an algorithm to find the average of a series of numbers that are read from the keyboard: [`average_numbers.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_2/average_numbers.py)

1. Given a series of real numbers that are being read from the keyboard, determine the maximum value and the 
position of it: [`position_largest_number.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_2/position_largest_number.py)

1. Write an algorithm that requests the reading of a series of individual characters and count how many times the 
letter "a" is entered. The user ends by entering the "$" symbol: [`count_a.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_2/count_a.py)

1. Develop an algorithm to count the number of students whose weight is between 50 and 60, between 61 and 80 
and between 81 and 100. The weights are entered by keyboard and report the number of students in each 
category of weight: [`category_of_weight.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_2/category_of_weight.py)

1. Write an algorithm to determine if a number read by keyboard is prime: [`prime_number.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_2/prime_number.py)

1. Write an algorithm to print and count numbers that are multiples of 2 or 3 that are between 1 and 100: [`count_multiples_two_three.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_2/count_multiples_two_three.py)

1. Develop an algorithm to determine if a series of numbers that the user is entering is in increasing order or not: [`increase_order.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_2/increase_order.py)

1. Develop an algorithm to count the number of students whose weight is between 50 and 60, between 61 and 80 and between 81 and 100. The weights are entered by keyboard and report to accumulate weight totals in each category of weight: [`accumulative_weight.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_2/accumulative_weight.py)

## Practice_3

1. Count the number of words, separated by one or more spaces, from a telegram ending in point. It can be assumed that the user enters character by character the telegram or the complete sequence, which is more comfortable to propose a solution: [`count_words.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_3/count_words.py)

1.	Develop an algorithm for a dice game. The player must bet on a number between 1 and 6 (keyboard reading), then you must simulate the roll of a dice and finally inform the player if he has won or lost: [`dice_game.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_3/dice_game.py)

1. Write an algorithm to invert a string of characters: [`invert_a_string.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_3/invert_a_string.py)

1.	Write a sub-algorithm that has a parameter of type number that represents a year and determines whether the year is leap year or not: [`leap_year.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_3/leap_year.py)

1. Write a sub-algorithm to determine the number of days of a month of a year, the latter two parameters of the sub-algorithm: [`month_year.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_3/month_year.py)

1.	A meteorological station collects rain data for a month and year of a determined locality. An algorithm must be written asking the user to enter a month and a year, and allow for each day of that month in that year, enter the millimeters of water that were recorded (in case of not having registered a rain one day is entered 0) . The amount of total millimeters of water precipitated in that month must be shown, the maximum precipitation recorded for a day and on what day it was given, and finally if it rained two days in a row: [`rain_data.py`](https://github.com/AmandaArenales/ComIT_Exercises_Python/blob/main/Practice_3/rain_data.py)


