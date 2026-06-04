import random

user_score = 0
computer_score = 0

while True:
    choices = ["rock", "paper", "scissors"]

    user = input("\nEnter rock, paper, or scissors: ").lower()
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1

    elif user in choices:
        print("Computer Wins!")
        computer_score += 1

    else:
        print("Invalid Choice")
        continue

    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    again = input("Play Again? (yes/no): ").lower()

    if again != "yes":
        break

print("Game Over")
