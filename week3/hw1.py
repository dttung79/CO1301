p = float(input('Enter principal amount: '))
r = float(input('Enter annual interest rate: '))
n = int(input('Enter number of times the interest is compounded per year: '))
t = int(input('Enter time the money is invested for: '))

A = p * (1 + r / n) ** (n * t)
    
print('The amount of money after', t, 'years is', A)
print(f'The amount of money after {t} years is {A}')