import random

def guess_number_game():
    """Play a guess number game where the user tries to guess a randomly generated number."""
    number_to_guess = random.randint(1, 100)
    guesses = 0
    valid_guesses = 0
    print("Guess the number between 1 and 100!")

    while True:
        try:
            guess = int(input("Enter your guess (or -1 to quit): "))
            if guess == -1:
                print("Exiting the game.")
                break
            guesses += 1
            valid_guesses += 1
            
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {guesses} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    score = max(0, valid_guesses - guesses)
    print(f"Your score: {score}")


def rock_paper_scissors():
    """Play a text-based rock-paper-scissors game against a computer opponent."""
    choices = ['rock', 'paper', 'scissors']
    user_wins = 0
    rounds = 0

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        if user_choice == 'exit':
            print("Exiting the game.")
            break
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        rounds += 1

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
            user_wins += 1
        else:
            print("You lose this round!")

    print(f"Total rounds played: {rounds}, Total wins: {user_wins}")


def trivia_pursuit():
    """Play a trivia pursuit quiz game with multiple choice questions."""
    questions = {
        "Science": [
            {"question": "What is the chemical symbol for water?", "options": ["A) H2O", "B) O2", "C) CO2"], "answer": "A"},
            {"question": "What planet is known as the Red Planet?", "options": ["A) Earth", "B) Mars", "C) Jupiter"], "answer": "B"}
        ],
        "History": [
            {"question": "Who was the first President of the United States?", "options": ["A) Abraham Lincoln", "B) George Washington", "C) Thomas Jefferson"], "answer": "B"},
            {"question": "In which year did the Titanic sink?", "options": ["A) 1912", "B) 1905", "C) 1920"], "answer": "A"}
        ]
    }

    score = 0

    for category, q_list in questions.items():
        print(f"\nCategory: {category}")
        for q in q_list:
            print(q["question"])
            for option in q["options"]:
                print(option)
            answer = input("Your answer (A, B, C): ").upper()
            if answer == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"Your total score: {score}")


def pokemon_card_binder_manager():
    """Manage a simple Pokemon card binder."""
    binder = []

    while True:
        action = input("Enter 'add' to add a card, 'view' to view cards, or 'exit' to quit: ").lower()
        if action == 'exit':
            print("Exiting the binder manager.")
            break
        elif action == 'add':
            card_name = input("Enter the name of the Pokemon card: ")
            binder.append(card_name)
            print(f"Added {card_name} to the binder.")
        elif action == 'view':
            if binder:
                print("Your Pokemon Card Binder:")
                for card in binder:
                    print(f"- {card}")
            else:
                print("Your binder is empty.")
        else:
            print("Invalid action. Please try again.")


def main():
    """Main function to run the command-line program."""
   