import random
import turtle

t=turtle.Pen()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")
colors = ["red","yellow","green","white","orange","purple","blue","gray"]

def draw_keleido (x,y):
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    draw_spiral(x,y, size)
    draw_spiral(-x,y, size)
    draw_spiral(-x,-y, size)
    draw_spiral(x,-y, size)

def draw_spiral (x,y, size):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range (size):
        t.forward(m*2)
        t.left(92)

turtle.onscreenclick(draw_keleido)
input("vbfg")