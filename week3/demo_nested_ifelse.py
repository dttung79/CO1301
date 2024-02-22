bus_price = int(input('Enter bus price: '))
age = int(input('Enter your age: '))
student = input('Are you a student? (yes/no): ')

# check if the user is a student
if student == 'yes':
    if age < 25:
        bus_price = bus_price * 0.5
        print('You get 50% discount')
    else:
        bus_price = bus_price * 0.75
        print('You get 25% discount')
else:
    if age < 18 or age > 65:
        bus_price = bus_price * 0.75
        print('You get 25% discount')

print(f'Your bus price is: {bus_price}')