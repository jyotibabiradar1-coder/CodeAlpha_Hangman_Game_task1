"""
CodeAlpha Internship - Task 1: Hangman Game
Author: Intern
Description: A simple text-based Hangman game where the player guesses a secret word
             one letter at a time with a maximum of 6 incorrect attempts.
Key Concepts Used: random, while loop, if-else, strings, lists.
"""

import random

# Predefined list of 5 words as per project specifications
WORDS = ["python", "developer", "coding", "alpha", "software"]

# ASCII art stages corresponding to 0 to 6 incorrect guesses
HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    =========
    """
]

MAX_INCORRECT_GUESSES = 6


def get_display_word(secret_word, guessed_letters):
    """
    Returns the secret word representation with guessed letters revealed
    and unrevealed letters shown as underscores.
    """
    display = []
    for letter in secret_word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    return " ".join(display)


def play_game():
    """Runs a single round of the Hangman game."""
    # Select a random word from the predefined list
    secret_word = random.choice(WORDS).lower()
    guessed_letters = []
    incorrect_guesses = 0

    print("\n" + "=" * 50)
    print("        WELCOME TO CODEALPHA HANGMAN GAME")
    print("=" * 50)
    print(f"Goal: Guess the secret word one letter at a time.")
    print(f"You are allowed a maximum of {MAX_INCORRECT_GUESSES} incorrect guesses.\n")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        # Display current hangman visual
        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"Word: {get_display_word(secret_word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining lives: {MAX_INCORRECT_GUESSES - incorrect_guesses}\n")

        # Get player input
        guess = input("Enter a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("\n[!] Invalid input. Please enter a single alphabetical letter.\n")
            continue

        if guess in guessed_letters:
            print(f"\n[!] You have already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.append(guess)

        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"\n[+] Good job! '{guess}' is in the secret word!")
        else:
            incorrect_guesses += 1
            print(f"\n[-] Sorry, '{guess}' is not in the secret word.")

        # Check for win condition (all letters guessed)
        word_completed = all(letter in guessed_letters for letter in secret_word)
        if word_completed:
            print(HANGMAN_STAGES[incorrect_guesses])
            print("=" * 50)
            print("*** CONGRATULATIONS! YOU WON! ***")
            print(f"The secret word was: {secret_word.upper()}")
            print("=" * 50)
            return

    # If loop ends, player ran out of lives
    print(HANGMAN_STAGES[MAX_INCORRECT_GUESSES])
    print("=" * 50)
    print(">>> GAME OVER! YOU RAN OUT OF GUESSES. <<<")
    print(f"The secret word was: {secret_word.upper()}")
    print("=" * 50)


def main():
    """Main function to handle game loops and replay option."""
    while True:
        play_game()
        replay = input("\nWould you like to play again? (y/n): ").strip().lower()
        if replay not in ("y", "yes"):
            print("\nThank you for playing CodeAlpha Hangman! Goodbye!\n")
            break


if __name__ == "__main__":
    main()
