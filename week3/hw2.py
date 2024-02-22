m = int(input('Enter number of minutes: '))

h = m // 60
m = m % 60

if h == 0:
    print(f'{m} Minutes')
elif m == 0:
    print(f'{h} Hours')
else:
    print(f'{h} Hours, {m} Minutes')