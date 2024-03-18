budget = 0
shopping = True

for i in range(1,8):
    print(f'Shopping day {i}')
    shopping = True
    budget = 0
    while shopping:
        grocery = input('Enter grocery name: ')
        price = float(input('Enter price: '))
        budget += price
        answer = input('Continue? (y/n): ')
        if answer == 'n':
            shopping = False
        

    print(f'Total for day {i}: {budget}')