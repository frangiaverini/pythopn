from turtle import *

def draw_square(side_length, color):
    pencolor(color)
    for i in range(4):
        forward(side_length)
        left(90)
    pencolor("black")
        
draw_square(200,"red")
draw_square(50, "blue")
draw_square(100, "green")
draw_square(150, "orange")


penup()
forward(50)
pendown()


def draw_triangle(side_length):
    for i in range(3):
        forward(side_length)
        left(120)

        
draw_triangle(200)
draw_triangle(50)
draw_triangle(100)
draw_triangle(150)
