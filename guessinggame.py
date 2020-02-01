import random
The_Number = random.randint(1 , 10)
guess = int(input("Guess a number between 1 to 10:"))
while guess != The_Number:
    if guess > The_Number:
        print(guess, " was too high . Try again")
    if guess < The_Number:
        print(guess ," was too low . Try again")
    guess = int(input("Guess again:"))
print(guess, " was the number! YOU WiN!")