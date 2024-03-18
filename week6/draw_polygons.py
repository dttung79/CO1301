import turtle as t
# Define a function called draw_polygon that takes two parameters: k and s. 
# The function should draw a polygon with k sides of length s.
def draw_polygon(k, s):
    for i in range(k):
        t.forward(s)
        t.right(360/k)

# Define a function called draw_n_polygons that takes three parameters: n, k, and s.
# The function should draw n polygons with k sides of length s.
def draw_n_polygons(n, k, s):
    for i in range(n):
        draw_polygon(k, s)
        t.right(360/n)

# Main program
n = int(input('Enter number of polygons: '))
k = int(input('Enter number of sides: '))
s = int(input('Enter length of sides: '))
t.speed(0)
draw_n_polygons(n, k, s)
t.exitonclick()