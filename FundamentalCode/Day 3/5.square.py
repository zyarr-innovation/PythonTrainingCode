
import turtle 
pen = turtle.Pen()
colors = ["red", "yellow", "blue", "green"]


for x in range (100):
    pen.pencolor(colors [x % 4])
    pen.forward(x * 4)
    pen.left(90) 