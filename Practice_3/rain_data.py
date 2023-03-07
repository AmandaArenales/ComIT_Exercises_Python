"""A meteorological station collects rain data for a month and year of a determined locality.
An algorithm must be written asking the user to enter a month and a year, and allow for each day 
of that month in that year, enter the millimeters of water that were recorded (in case of not having 
registered a rain one day is entered 0) . The amount of total millimeters of water precipitated in that 
month must be shown, the maximum precipitation recorded for a day and on what day it was given, 
and finally if it rained two days in a row."""

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
        print("Please, verify if you inserted correctly the month and the year. \n")
        return
    print(f'\nThe {month} of {year} has {days} days.')
    return days
    
month = input("Please, insert a month: ")
year = int(input("\nPlease, insert a year: "))
list_month_ml_water = []
d = 0

days = days_month_year(month, year)

print("\nNow, you will be request to enter the millimeters of water that were recorded every day" 
      + " insert 0 in case of not having registered a rain. \n")

while d < days:
    d = d + 1
    ml_water_day = int(input("Please, insert the millimeters of water that was recorded"
                     + f" on {d} of {month} of {year}: "))
    list_month_ml_water.append(ml_water_day)
    

total_preciptation = sum(list_month_ml_water)
print(f"\nThe amount of total millimeters of water precipitated in {month} of {year} was: {total_preciptation}.")

max_preciptation = max(list_month_ml_water)
day_max_prec = list_month_ml_water.index(max_preciptation) + 1

print(f"\nThe maximum precipitation recorded for a day was {max_preciptation} and it happened on day {day_max_prec}. \n")

rain_row = False
for i in range(1, len(list_month_ml_water)):
    if (list_month_ml_water[i] != 0) and (list_month_ml_water[i-1] != 0):
        rain_row = True

if rain_row == True:
    print (f"During {month} of {year} has rained two days in a row. \n")
else:
    print (f"During {month} of {year} hasn't rained two days in a row. \n")
