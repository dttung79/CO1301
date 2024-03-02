# Ask user to enter number n
# Ask user to enter n fruits
# Count how many fruits are apples / bananas

counter = 0
n = int(input('Enter number n: '))
for i in range(n):
    fruit = input('Enter a fruit: ')
    if fruit == 'apple' or fruit == 'banana':
        counter += 1

print(f'You have {counter} apples or bananas among {n} fruits')