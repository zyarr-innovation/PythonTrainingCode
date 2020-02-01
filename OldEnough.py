driving_age = eval(input ("what is your legal driving age in your area ?"))
your_age = eval (input ("what is your age ?"))
if your_age >= driving_age:
    print ("you are old enough to drive")
if your_age < driving_age:
    print ("sorry you are having ", driving_age - your_age ,"years"  )      
    