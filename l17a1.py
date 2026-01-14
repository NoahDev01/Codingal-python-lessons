import random
playing=True
number=str(random.randint(0,9))
print("guess the number from 0 to 9 to win the game")
while playing:
    guess=input("guess a number from 0 to 9")
    if guess==number:
        print("you won the game")
        break
    else:
        print("try again")
        
    
        