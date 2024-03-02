status = input('Enter your member status (gold/silver/none): ')
order = float(input('Enter your order amount: '))

if status != 'gold' and status != 'silver' and status != 'none':
    print('Invalid status')
else:
    if status == 'gold':
        discount = 15 if order > 500 else 10
    elif status == 'silver':
        discount = 10 if order > 500 else 5
    else:
        discount = 2 if order > 500 else 0
    
    print(f'Discount: {discount}%')
    order = order - (order * discount / 100)
    print(f'Order amount after discount: ${order:.2f}')