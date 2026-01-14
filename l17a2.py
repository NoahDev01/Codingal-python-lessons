import random
while True:
    action=input("you can choose rock,paper,sciccors")
    guess=["rock", "paper", "sciccors"]
    computer=random.choice(guess)
    print("\nyour choice", action)
    print("\nComputer choice", computer)
    if action == computer:
        print("its a tie")
    elif action == "rock":
        if computer =="paper":
            print("computer wins")
        else:
            print("you win")
    elif action == "sciccors":
        if computer == "paper":
            print("u win")
        else:
            print("computer wins")
    elif action == "paper":
        if computer == "rock":
            print("u win")
        else:
            print("computer wins") 
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break 
       
            
        

    