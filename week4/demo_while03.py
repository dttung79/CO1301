# Keep entering numbers until the user enters zero
# Count how many even numbers entered
# counter = 0
# n = int(input('Enter a number: '))

# while n != 0:
#     if n % 2 == 0:
#         counter += 1 
    
#     n = int(input('Enter a number: '))

# print(f'You entered {counter} even numbers')

# Ask user enter a kind of fruit, stop when user type 'quit'
# Count how many banana and apple are entered?

counter = 0
fruit = input('Enter a fruit: ')

while fruit != 'quit':
    if fruit == 'banana' or fruit == 'apple':
        counter += 1
    
    fruit = input('Enter a fruit: ')

print(f'You entered {counter} bananas and apples')