"""Write a program that allows you to enter the height of 10 students, 
then show the average height, and how many elements are above average, 
how many are below average."""

student_heights = []
above_average = 0
below_average = 0

for student in range(1, 11):
    height =  float(input(f"Please, insert the sutdent {student} height: "))
    student_heights.append(height)

avg_height = sum(student_heights) / len(student_heights)

for height_compare in student_heights:
    if height_compare >= avg_height:
        above_average = above_average + 1
    else:
       below_average = below_average + 1
       
print(f"There are {above_average} students which their height is above average!")

print(f"There are {below_average} students which their height is below average!")