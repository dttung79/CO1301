n = int(input('Enter n: '))
for i in range(1, n+1):
    # print i - 1 spaces
    for j in range(i - 1):
        print(' ', end=' ')
    # print 2(n - i) + 1 stars
    for j in range(2 * (n - i) + 1):
        print('*', end=' ')
    print()

print('------')
for i in range(n):
    # print i - 1 spaces
    for j in range(n - i - 1):
        print(' ', end=' ')
    # print i + 1 stars
    for j in range(i + 1):
        print('*', end=' ')
    print()
