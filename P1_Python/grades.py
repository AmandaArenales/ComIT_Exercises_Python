"""Make a program in Python such that given as data the 
enrolment and 5 grades of a student; Print the enrolment, 
the average and the word "approved" if the student has an average greater 
than or equal to 6, and the word "not approved" otherwise. 
Data: MAT, CAL1, CAL2, CAL3, CAL4, CAL5 Where: MAT is an integer variable that 
represents the student's enrolment. CAL1, CAL2, CAL3, CAL4 and CAL5 are real-type 
variables representing the student's 5 grades."""

grades = ["CAL1", "CAL2", "CAL3", "CAL4", "CAL5"]
grade_list = []

for grade in grades:
    grade =  float(input(f"Please, insert the sutdent grade in {grade}: "))
    grade_list.append(grade)

avg_grade = sum(grade_list) / len(grade_list)

if avg_grade >= 6:
    print(f"The student grade in MAT is {avg_grade} and the student is approved!")
else:
    print(f"The student grade in MAT is {avg_grade} and the student is not approved!")