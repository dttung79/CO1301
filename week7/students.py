names = []
grades = []

def max_index(numbers):
    max_pos = 0
    greatest = numbers[max_pos]
    for i in range(len(numbers)):   # loop through the indexes of the list
        if numbers[i] > greatest:
            greatest = numbers[i]
            max_pos = i
    
    return max_pos

n = int(input('Enter number of students: '))
for i in range(n):
    name = input('Enter name of student: ')
    grade = float(input('Enter grade of student: '))
    # add name and grade to the lists
    names.append(name)
    grades.append(grade)

# print students and their grades
for i in range(n):
    print(f'{names[i]}: {grades[i]:.2f}')
# find the student with the highest grade
# max_pos = 0
# max_grade = grades[0]

# for i in range(n):
#     if grades[i] > max_grade:
#         max_grade = grades[i]
#         max_pos = i
max_pos = max_index(grades)
print(f'Student {names[max_pos]} has the highest grade: {grades[max_pos]:.2f}')