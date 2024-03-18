import turtle as t
import random as rd


n = int(input('Enter n: '))
#length = int(input('Enter length: '))

t.speed(0)
t.colormode(255)

for i in range(n):
    t.color(rd.randint(0,255), rd.randint(0,255), rd.randint(0,255))
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.right(360/n)

t.exitonclick()