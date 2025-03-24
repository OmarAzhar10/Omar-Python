# for square

import turtle

# turtle setup
pen = turtle.Turtle()
pen.speed(2)
pen.color("red")
pen.fillcolor("cyan")

pen.begin_fill()

for _ in range(4):
    pen.forward(100)
    pen.right(90)

pen.end_fill()

turtle.done()