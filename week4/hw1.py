location = input('Enter location: ')
order_amount = int(input('Enter order amount: '))

if location != 'USA' and location != 'Canada' and location != 'International':
    print('Invalid location')
else:
    fee = 0
    if location == 'USA':
        if order_amount <= 50:
            fee = 5
    elif location == 'Canada':
        if order_amount <= 100:
            fee = 10
    elif location == 'International':
        if order_amount <= 200:
            fee = 20
    
    print('Shipping fee:$', fee)
