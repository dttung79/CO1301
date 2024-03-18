def my_max(a, b):
    if a > b:
        return a
    return b

def my_max_3_v1(a, b, c):
    if a >= b:
        if a >= c:
            return a  
        return c
    elif b >= c:
        return b
    
    return c

def my_max_3_v2(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= c and b >= a:
        return b
    return c

def my_max_3_v3(a, b, c):
    # m = my_max(a, b)
    # n = my_max(m, c)
    # return n
    return my_max(my_max(a, b), c)

x = int(input('Enter x: '))
y = int(input('Enter y: '))
z = int(input('Enter z: '))

print(f'Max 3 numbers {my_max_3_v1(x, y, z)}')
print(f'Max 3 numbers {my_max_3_v2(x, y, z)}')
print(f'Max 3 numbers {my_max_3_v3(x, y, z)}')