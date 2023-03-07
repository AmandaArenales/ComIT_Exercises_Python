"""Develop an algorithm to count the number of students whose weight is between 50 and 60, 
between 61 and 80 and between 81 and 100. The weights are entered by keyboard and report 
the number of students in each category of weight."""

def category_of_weight():
    students = int(input("How many students do you have? "))
    student = 0
    count = 1
    cat_50_60 = 0
    cat_61_80 = 0
    cat_81_100 = 0

    while student < students:
        weight = int(input(f"Please, insert the weight of the student {count}:"))
        
        if 50 <= weight <= 60:
            cat_50_60 = cat_50_60 + 1        
        elif 61 <= weight <= 80:
            cat_61_80 = cat_61_80 + 1        
        elif 81 <= weight <= 100:
            cat_81_100 = cat_81_100 + 1
        else:
            print("This weight is invalid!")
            continue # stops the looping and goes to the next iteration
        
        count = count + 1
        student = student + 1

    print(f"There are {cat_50_60} students whose weight is between 50 and 60.")
    print(f"There are {cat_61_80} students whose weight is between 61 and 80.")
    print(f"There are {cat_81_100} students whose weight is between 81 and 100.")

category_of_weight()

    
