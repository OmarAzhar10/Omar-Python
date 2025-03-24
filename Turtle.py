#spiral

import turtle

pen = turtle.Turtle()
turtle.bgcolor("black")

pen.color("blue")
pen.pensize(3)
pen.speed(5)

for i in range(100):
    pen.forward(i * 2)
    pen.right(45)

turtle.done()