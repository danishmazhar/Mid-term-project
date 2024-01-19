import random

print("Welcome to Rock, Paper, Scissors Game!")

while True:
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}\n")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing. Goodbye!")
        break
