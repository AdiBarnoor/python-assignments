import random

# Generate a random number between 1-20
def generate_random_number():
    return random.randint(1, 20)

# Recieves user input
def get_user_input():
    guess = input("Enter your guess (or 'x' - exit, 'n' - new game, 's' - show number): ").strip().lower()
    return guess

# Check if the guess is bigger or smaller then the random number
def Check_Guess(guess, num, guesses):
    if guess < num:
        print("Too small!")
    elif guess > num:
        print("Too big!")
    else:
        print(f"Exact! You've guessed the number in {guesses} tries.")
        return "won"
    return
    
# Plays a single round of the guessing game
def play_game():
    secret_number = generate_random_number()
    print("\nI have thought of a number between 1 and 20.")
    print("You can guess it or type 'x' to exit, 'n' to start a new game, 's' to cheat.")
    
    guesses = 0
    while True:
        guess = get_user_input()
        
        if guess == 'x':  # Exit the game
            print("Exiting the program. Goodbye!")
            return "exit"
        elif guess == 'n':  # Start a new game
            print("You chose to start a new game!")
            return "new_game"
        elif guess == 's':  # Show the hidden number
            print(f"The hidden number is: {secret_number}")
            continue
        
        # Validate input
        if not guess.isdigit():
            print("Invalid input. Please enter a whole number between 1 and 20.")
            continue

        # Convert to integer and process the guess
        guess = int(guess)
        guesses += 1

        check = Check_Guess(guess, secret_number, guesses)
        if(check == "won"):
            return "won"

# Main function - handles multiple games
def main():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        result = play_game()
        
        if result == "exit":
            break
        elif result == "new_game":
            continue  # Start a new game
        else:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for playing! Goodbye!")
                break

if __name__ == "__main__":
    main()        