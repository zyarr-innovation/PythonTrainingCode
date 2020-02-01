import turtle
t=turtle.Pen()
#turtle.bgcolor("black")
t.speed(0)
t.hideturtle()
def draw_smiley(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    #HEAD
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    #LEFT EYE
    t.setpos(x-15,y+60)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    #RIGHT EYE
    t.setpos(x+15,y+60)
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    #MOUTH
    t.setpos(x-25, y+40)
    t.pencolor("black")
    t.width(10)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+25, y+40)
    t.width(1)
for n in range(50):
    x = -turtle.window_width()//2,turtle.window_width()//2
    y = -turtle.window_height()//2,turtle.window_height()//2
    draw_smiley(x,y)
input("jahsg")