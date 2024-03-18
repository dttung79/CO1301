from random import randint

playing = True

while playing:
    balance = int(input('Deposit amount: '))
    while balance > 0:
        bet = input('Choose odd or even: ')
        n = randint(1, 100)
        if n % 2 == 0 and bet == 'even' or n % 2 != 0 and bet == 'odd':
            print(f'You won! The number is {n}')
            balance += 10
        else:
            print(f'You lost! The number is {n}')
            balance -= 10
        print(f'Current balance: {balance}')
        
        answer = input('Do you want to stop? (y/n): ')
        if answer == 'y':
            playing = False
            break
    
    # out of balance, ask user to play again
    print('Out of balance')
    balance = int(input('Deposit amount (0 to quit): '))
    playing = balance > 0

print(f'Final balance: {balance}')
