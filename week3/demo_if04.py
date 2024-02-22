gpa = int('Enter GPA: ')

if gpa < 0 or gpa > 100:
    print('Invalid GPA, must be between 0 and 100')
elif gpa >= 80:
    print('Distinction')
elif gpa >= 60:
    print('Merit')
elif gpa >= 40:
    print('Pass')
else:
    print('Fail')