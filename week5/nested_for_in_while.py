n = int(input('Enter n: '))

# while n > 0:
#     for i in range(n):
#         for j in range(n - i - 1):
#             print(' ', end=' ')
#         for j in range(i + 1):
#             print('*', end=' ')
#         print()
    
#     n = int(input('Enter n to draw another triangle: '))

# while n > 0:
#     s = 0
#     for i in range(1, n + 1):
#         s += i
#     print(f'Sum from 1 to {n} = {s}')

#     n = int(input('Enter n to calculate another sum: '))

printing = True

while printing:
    n = int(input('Enter number n: '))

    for i in range(1, 11):
        print(f'{i:2} x {n} = {i * n}')

    answer = input('Continue? (y/n) ')
    printing = answer == 'y'