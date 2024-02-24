import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:

    user_input = input("Type Rock/Paper/Scissors or Q to quit:   ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue


    random_number = random.randint(0,2)
    # rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    print("computer picks", computer_pick,  ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you win")
        user_wins +=1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("you win")
        user_wins +=1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("you win")
        user_wins +=1
    
    elif user_input == computer_pick:
        print("its a tie go again")
        continue
    else:
        print("you lost")
        computer_wins += 1
        continue

print("The number of user wins: ", user_wins, " and number of computer wins: " , computer_wins)

print("Goodbye!")
