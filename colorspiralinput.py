import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "blue", "green", "yellow", "orange", "purple", "white", "gray"]
sides = int(turtle.numinput("number of sides", "How many sides do you want(1-8)"))
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
input("Yusuf")