import turtle as t

length = int(input('Enter the length: '))
n = int(input('Enter the number of sides: '))

for i in range(n):
    t.forward(length)
    t.backward(length)
    t.right(360 / n)

t.exitonclick()