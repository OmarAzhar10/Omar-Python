 # polygon

import turtle

pen = turtle.Turtle()

pen.speed(2)
pen.color("green")
pen.fillcolor("yellow")
pen.begin_fill()

number_of_sides = 6
side_length = 80

for _ in range(number_of_sides):
    pen.forward(side_length)
    pen.right(360 / number_of_sides)

pen.end_fill()

turtle.done