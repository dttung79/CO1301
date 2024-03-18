import turtle as t

def draw_square(s):
    for i in range(4):
        t.forward(s)
        t.right(90)

def draw_n_squares(n, s):
    for i in range(n):
        draw_square(s)
        t.right(360/n)

n = int(input('Enter n: '))
s = int(input('Enter square size: '))
t.speed(0)

draw_n_squares(n, s)

t.exitonclick()