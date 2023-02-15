import random

win_result = {
    "paper" : "rock",
    "rock"  : "scissor",
    "scissor" : "paper",
}

options = ["paper", "rock", "scissor"]

def start_game():
    while True:
        pc = random.choice(options)
        player = input("Please input rock, paper, or scissor\n")
        print(pc)
        if pc == player :
            print("Tie")
        elif win_result[pc] == player:
            print("You lose")
        else:
            print("You win")
    return 0

if __name__ == "__main__":
    start_game()