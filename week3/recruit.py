name = input('Enter your name: ')
years = int(input('Enter years of experience: '))
language = input('Enter your programming language: ')

if language != 'C' and language != 'Java':
    print('Sorry, we only accept C and Java programmers')
elif years < 2:
    print('Sorry, you need at least 2 years of experience')
else:
    # if language == 'C':
    #     project = 'System'
    # else:
    #     project = 'Web'
    project = 'System' if language == 'C' else 'Web'
    
    # if years <= 3:
    #     position = 'Junior'
    # else:
    #     position = 'Senior'
    position = 'Junior' if years <= 3 else 'Senior'
    
    print(f'You are accepted as a {position} {project} developer')