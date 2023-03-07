"""(Poll.py) A survey was carried out to 15 students in a University where the following 
information was requested: Photo ID #, SEX, SALARY, JOB.

• PHOTO ID # (It's an integer)
• SEX (1 - Male 2 - Female)
• JOB (1 - If you work 2 - Do not work)
• SALARY (An integer value)

Write the algorithm that allows reading and storing the requested data in vectors, then calculate and print:

• Percentage of men in the university
• Percentage of women in the university
• Percentage of men who work and average salary
• Percentage of working women and average salary"""

student_info = []
student = 0
total_student_men = 0
total_student_women = 0
total_work_men = 0
total_work_women = 0
sum_salary_men = 0
sum_salary_women = 0 

while student < 15:
    student = student + 1
    photo_ID = int(input(f"\nPlease, insert a photo ID of student {student}: "))
    sex = int(input(f"Please, insert a sex (1 - Male 2 - Female) of student {student}: "))
    job = int(input(f"Please, insert a job (1 - If you work 2 - Do not work) of student {student}: "))
    salary = int(input(f"Please, insert a salary of student {student}: "))

    d = {}
    d['Photo ID'] = photo_ID
    d["Sex"] = sex
    d["Job"] = job
    d["Salary"] = salary

    student_info.append(d)

for s in student_info:
    if s["Sex"] == 1:
        total_student_men +=  1
        if s["Job"] == 1:
            total_work_men += 1
            sum_salary_men += s["Salary"]
    else:
        total_student_women += 1
        if s["Job"] == 1:
            total_work_women += 1
            sum_salary_women += s["Salary"]

percentage_men = (total_student_men/student) * 100

print(f"\nThe percentage of men in the university is {percentage_men}")

percentage_women = (total_student_women/student) * 100

print(f"\nThe percentage of women in the university is {percentage_women}")

percentage_men_work = (total_work_men/total_student_men) * 100
avg_salary_men = sum_salary_men / total_work_men

print(f"\nThe percentage of men who work is {percentage_men_work} and average salary {avg_salary_men}")

percentage_women_work = (total_work_women/total_student_women) * 100
avg_salary_women = sum_salary_women / total_work_women

print(f"\nThe percentage of women who work is {percentage_women_work} and average salary {avg_salary_women}")
