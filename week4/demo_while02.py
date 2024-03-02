# Ask user to enter a positive number, if invalid, ask again
n = 0

while n <= 0:
    n = int(input('Enter a positive number: '))
    if n <= 0:
        print('Invalid number')

print(f'Here is the positive number {n}')