import random
choosenNum = random.randint(1,10)
guessNum = -1
while guessNum != choosenNum:
    guessNum = eval (input("Guess the number"))
    if guessNum > choosenNum:
        print("Your guess is high")
    elif guessNum < choosenNum:
        print("Your guesss is low")
 
print("Your guess is correct: ", choosenNum)
