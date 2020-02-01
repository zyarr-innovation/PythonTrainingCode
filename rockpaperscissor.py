import random
choices = ["rock" , "paper" , "scissor"]
print ("Rock crushes scissor , scissors cuts paper , paper covers rock")
player = input("Do you want to be rock paper scissor[or quit]")
while player != "quit":
    player = player.lower()
    computer = random.choice(choices)
    print("you chose " +player+ ", and computer chose " +computer+ ".")
    if player == computer:
        print("Its a tie")
    elif player == "rock":
        if computer == "scissor":
            print("You win!")
        else:
            print("computer wins!")
    elif player == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("Computer wins!")
    elif player == "scissor":
        if computer == "paper":
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("I think there was some sort of error....")
    print()
    player = input("Do you want to be rock , paper , scissor(or quit)")