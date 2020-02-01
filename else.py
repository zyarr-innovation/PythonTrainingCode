driving_age = eval(input("what is the legal age in your area to drive ? "))
your_age = eval(input("what is your age ?"))
if your_age >= driving_age :
    print("you are old enough to drive")
else :
    print("sorry you can drive in" ,driving_age-your_age,"years")