import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ['red','green','orange']
your_name = turtle.textinput("Enter your name", "What is your name?")
for x in range(50):
    t.pencolor(colors[x%3])
    t.penup()
    t.forward(x*6)
    t.pendown()
    t.write(your_name, font = ("Arial", int( (x + 2) / 2), "bold") )
    t.left(70)
input("p")