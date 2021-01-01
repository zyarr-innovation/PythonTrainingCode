import turtle
pen = turtle.Pen()
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
for x in range(100):
    pen.pencolor(colors[x % len(colors)])
    pen.forward(x * 10)
    pen.left(120)
