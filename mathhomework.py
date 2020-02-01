print("MathHomework.py")
problem = input("Enter a Math problem , or 'q' to quit")
while(problem != "Q"):
    print("The answer to ", problem,"is:", eval(problem))
    problem = input("Enter another Math problem,or 'q' to quit:")