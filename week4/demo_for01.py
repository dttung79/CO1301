# range function: generates a sequence of numbers
print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(1, 6))) # [1, 2, 3, 4, 5]
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]

output = ''
for i in range(4):
    output += '*'

print(output)