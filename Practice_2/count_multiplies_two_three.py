"""Write an algorithm to print and 
count numbers that are multiples of 2 or 3 that are between 1 and 100."""

def count_multiplies_two_three():
    count_multiplies = 0
    
    for number in range(1, 101):
        if ((number % 2) == 0) or ((number % 3) == 0):
            count_multiplies = count_multiplies + 1
    print (f"Between 1 and 100 there are {count_multiplies} numbers that are multiples of 2 or 3." )


count_multiplies_two_three()