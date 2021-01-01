
import turtle
pen = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
    pen.pencolor(colors[x % 4])
    pen.circle(x * 10)
    pen.left(91)
 
