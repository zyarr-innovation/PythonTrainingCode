import turtle
t = turtle.Pen()
number = int(turtle.numinput("Number of sides or circles" , "How many sides or circles do you want" , 6))
shape = turtle.textinput("Which shape do you want?" , "Enter'P' for polygon and 'R' for rosette:")
for x in range (number):
    if shape == 'R':
        t.circle(100)
    else:
        t.forward(150)
    t.left(360/number)
input("Byee")