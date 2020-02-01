import turtle
t=turtle.Pen()
turtle.bgcolor("black")
colors=["red","yellow","green","orange","white","gray","purple","pink","brown"]
family=[]
name = turtle.textinput("my name","enter a name,or just hit [enter] to quit")
while name !="":
    family.append(name)
    name = turtle.textinput("my name","enter a name ,or just hit [enter] to quit")
for x in range (50):
    t.pencolor(colors[x%len(family)])
    t.penup()
    t.forward(x*8)
    t.pendown()
    t.write(family[x%len(family)], font = ("Arial" , int((x*4)/4)))
    t.left(360/len(family)+2)
input("p")
