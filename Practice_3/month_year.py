"""Write a sub-algorithm to determine the 
number of days of a month of a year, the latter two parameters of the sub-algorithm."""

def days_month_year(month, year):

    months_31d = ["January", "March", "May", "July", "August", "October", "December"]
    months_30d = ["April", "June", "September", "November"]

    if month in months_31d:
        days = 31
    elif month in months_30d: 
        days = 30
    elif ((year % 4) == 0) and (month == "February"):
        days = 29
    elif ((year % 4) != 0) and (month == "February"):
        days = 28
    else:
        print("Please, verify if you inserted correctly the month and the year.")
        return
    print(f'The {month} of {year} has {days} days.')
    
    
month = input("Please, insert a month: ")
year = int(input("Please, insert a year: "))

days_month_year(month, year)