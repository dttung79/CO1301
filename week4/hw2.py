status = input('Enter your status (single/married): ')
income = float(input('Enter your income: '))

if status != 'single' and status != 'married':
    print('Invalid status')
else:
    tax = 24 # default tax rate
    if status == 'single':
        if income <= 9.875:
            tax = 10
        elif income <= 40.125:
            tax = 12
        elif income <= 85.525:
            tax = 22
    else:
        if income <= 19.75:
            tax = 10
        elif income <= 80.250:
            tax = 12
        elif income <= 171.050:
            tax = 22
    
    print(f'Tax rate: {tax}%')