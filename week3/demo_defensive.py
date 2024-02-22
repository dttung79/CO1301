a = int(input('Enter a: '))
b = int(input('Enter b: '))
operation = input('Enter operation (+, -): ')

# defensive programming: always check incorrect input first
if operation != '+' and operation != '-':
    print('Invalid operation')
elif operation == '+':
    print(f'{a} + {b} = {a + b}')
else:
    print(f'{a} - {b} = {a - b}')