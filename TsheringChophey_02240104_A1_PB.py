import random

def guess_number_game():
    print("Kuzuzangpo to Guess the Number Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            if user_guess < 1 or user_guess > 100:
                print("Please guess a number within the range!")
                continue
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Hooray! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def rock_paper_scissors_game():
    print("Kuzuzangpo to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()
        
        if user_choice == 'exit':
            print("Thanks for playing! You did great!")
            break
        
        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

def main():
    while True:
        print("\nMenu:")
        print("1. Guess the Number Game")
        print("2. Rock, Paper, Scissors Game")
        print("3. Exit")
        print("NO ONE IS PERFECT IN THIS WORLD")
        
        choice = input("Select a game (1-3): ")
        
        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors_game()
        elif choice == '3':
            print("Exiting the program. Have a good day!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 3.")

if __name__ == "__main__":
    main()