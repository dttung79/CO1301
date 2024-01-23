import math


for a in range(10):
    print(a)
    
name = input('Enter student name: ')
math = int(input('Enter math grade: '))
english = int(input('Enter english grade: '))
history = int(input('Enter history grade: '))

avg_grade = (math + english + history) / 3

print('Student: ', name)
print('Average grade: ', avg_grade)