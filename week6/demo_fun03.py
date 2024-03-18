# Write a program to enter name & 3 grades (math, english, physics) for 2 students
# and calculate the average grade for each student
# then compare the average grades and print which student is better

def avg_grades(math, english, physics):
    return (math + english + physics) / 3

def compare(name1, avg1, name2, avg2):
    if avg1 > avg2:
        return name1
    return name2

name1 = input("Enter name of student 1: ")
math1 = float(input("Enter math grade of student 1: "))
english1 = float(input("Enter english grade of student 1: "))
physics1 = float(input("Enter physics grade of student 1: "))

name2 = input("Enter name of student 2: ")
math2 = float(input("Enter math grade of student 2: "))
english2 = float(input("Enter english grade of student 2: "))
physics2 = float(input("Enter physics grade of student 2: "))

avg1 = avg_grades(math1, english1, physics1)
avg2 = avg_grades(math2, english2, physics2)

better_student = compare(name1, avg1, name2, avg2)
print(f'Student {better_student} has better average grade.')