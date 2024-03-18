n = int(input('Enter n: '))
m = int(input('Enter m: '))

for i in range(n):             # loop through each row
    for j in range(m):         # loop through each column
        print('*', end=' ')    # print a star without newline
    
    # after printing a row, print a newline
    print()