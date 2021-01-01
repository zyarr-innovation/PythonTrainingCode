import turtle
pen = turtle.Pen()
turtle.bgcolor("black")
 
# You can choose between 2 and 6 sides for some cool shapes!
sides = eval (input("Enter the number of sides"))
colors = ["red", "yellow", "blue", "orange", "green", "purple", "skyblue", "brown", "pink"]
 
for x in range(360):
    pen.pencolor(colors[x%sides])
    pen.forward(x * 6/sides + x)
    pen.left(360/sides)
    pen.width(x*sides/100)
