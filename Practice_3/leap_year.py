"""Write a sub-algorithm that has a parameter 
of type number that represents a year and determines whether the year is leap year or not.""" 

def leap_year(year):

    if (year % 4) == 0:
        print(f"The {year} is a leap year!")
    else:
        print(f"The {year} is not a leap year!")

year = int(input("Please, insert a year: "))
leap_year(year)

