import random
import turtle
t = turtle.Pen()
t.speed(-10000)
turtle.bgcolor("black")
colors = ["red","yellow","orange","white","green","grey","purple"]
for n in range (50):
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    x = random.randrange(0,turtle.window_width()//2)
    y = random.randrange(0,turtle.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range (size):
        t.forward (m*2)
        t.left (91)
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    for m in range (size):
        t.forward (m*2)
        t.left (91)
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    for m in range (size):
        t.forward (m*2)
        t.left (91)
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    for m in range (size):
        t.forward (m*2)
        t.left (91)
input("ppp")