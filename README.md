# Task 1: Hangman Game (Python)

A classic console-based **Hangman Game** built using Python as part of the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Overview
The Hangman game is a word-guessing game where the player attempts to guess a secret word by suggesting letters within a limited number of attempts. For every incorrect guess, a part of the hangman figure is drawn.

### Features
- **Predefined Word List**: Selects randomly from a curated list of words (`python`, `developer`, `coding`, `alpha`, `software`).
- **Visual ASCII Stages**: Dynamic ASCII art representation illustrating 0 through 6 incorrect attempts.
- **Input Validation**: Rejects invalid inputs (non-alphabetic characters, multiple characters) and alerts the user if a letter has already been guessed.
- **Game State Tracking**: Displays revealed letters, remaining lives, and previously guessed letters.
- **Replayability**: Option to play multiple rounds without restarting the script.

---

## 🛠️ Key Concepts Used
- `random.choice()` for secret word selection
- `while` loop for game loop and input validation
- `if-elif-else` conditional statements for game logic
- String operations (`.lower()`, `.strip()`, `.isalpha()`, `.join()`)
- Lists and list comprehension for tracking guessed letters and stages

---

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to this directory:
   ```bash
   cd Task1_Hangman_Game
   ```
3. Run the script:
   ```bash
   python hangman.py
   ```

---

## 🎮 Sample Gameplay

```text
==================================================
        WELCOME TO CODEALPHA HANGMAN GAME
==================================================
Goal: Guess the secret word one letter at a time.
You are allowed a maximum of 6 incorrect guesses.

       ------
       |    |
       |
       |
       |
       |
    =========
    
Word: _ _ _ _ _ _
Guessed letters: None
Remaining lives: 6

Enter a letter: p

[+] Good job! 'p' is in the secret word!

       ------
       |    |
       |
       |
       |
       |
    =========
    
Word: p _ _ _ _ _
Guessed letters: p
Remaining lives: 6
```
