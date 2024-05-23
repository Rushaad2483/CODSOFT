from random import randint

#moves for the player
moves = ["rock","paper","scissors"]
score_p=0
score_c=0
running =True
while running:
    
    computer = moves[randint(0,2)]
    player = input("Enter a choice (rock, paper or scissors):  ").lower()

    print(f"Player: {player}")
    
    
    if player == computer:
        print(f"Computer: {computer}")
        print(f"It's a Tie!")
        
    elif player=="rock":
        if computer == "paper":
            print(f"Computer: {computer}")
            print(f"You lose!")
            
            score_c=score_c+1
            
        else:
            print(f"Computer: {computer}")
            print(f"You Win!")
            
            score_p=score_p+1
           
    elif player=="paper":        
        if computer == "scissors":
            print(f"Computer: {computer}")
            print(f"You lose!")
            
            score_c=score_c+1
            
        else:
            print(f"Computer: {computer}")
            print("You Win!")
            
            score_p=score_p+1
            
    elif player=="scissors":
        if computer == "rock":
            print(f"Computer: {computer}")
            print("You lose!")
            
            score_c=score_c+1
            
        else:
            print(f"Computer: {computer}")
            print("You Win!")
            
            score_p=score_p+1
            
    else:
        print("Input entered is incorrect")
    print("Score", score_p, "-", score_c)

    if not input("Play again? (y/n): ").lower() == "y":
        running = False
        print("The game has ended")