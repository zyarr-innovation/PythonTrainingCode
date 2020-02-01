Answer = input("Do you want to see a spiral ? , y/n")
if Answer == 'y':
    print("Working...")
    import turtle
    t = turtle.Pen()
    turtle.bgcolor("green")
    t.width(2)
    for x in range (100):
        t.forward(x * 2)
        t.left(89)
print("Okay , We are done!")