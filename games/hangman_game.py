"""Terminal-based hangman game with difficulty levels."""

import os
import random

# ASCII art for the hangman stages.
HANGMAN_PICS = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
      /    |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
      / \\  |
          |
    ========='''
]

WORD_CATEGORIES = {
    "easy": [
        "cat", "dog", "fish", "apple", "banana", "grape", "kiwi", "lemon",
        "rose", "tulip", "sun", "moon", "star", "red", "blue", "green",
        "happy", "sad", "love", "joy", "peace", "life", "city", "town"
    ],
    "medium": [
        "cherry", "date", "fig", "mango", "orange", "papaya", "quince",
        "guitar", "piano", "drum", "mountain", "river", "ocean", "forest",
        "pizza", "burger", "pasta", "jacket", "shirt", "pants", "dress",
        "science", "math", "history", "geography", "literature"
    ],
    "hard": [
        "elderberry", "nectarine", "raspberry", "strawberry", "watermelon",
        "helicopter", "motorcycle", "computer", "smartphone", "television",
        "adventure", "exploration", "friendship", "imagination", "creativity",
        "technology", "engineering", "sustainability", "independence",
        "collaboration", "opportunity", "resilience", "authenticity"
    ]
}


def clear_screen():
    """Clear the terminal screen for a cleaner game display."""
    os.system("cls" if os.name == "nt" else "clear")


def show_instructions():
    """Display the game's rules and pause before starting."""
    print("\nInstructions: Guess the word letter by letter. You have a limited number of tries.\n")
    input("Press [Enter] to continue.")
    clear_screen()


def select_difficulty():
    """Let the user choose easy, medium, or hard difficulty."""
    while True:
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
        if difficulty in WORD_CATEGORIES:
            return difficulty

        input("Invalid choice. Please select easy, medium, or hard.")
        clear_screen()


def get_random_word(difficulty):
    """Return a random word from the selected difficulty category."""
    return random.choice(WORD_CATEGORIES[difficulty])


def display_hangman(tries):
    """Display the hangman figure based on the number of wrong guesses."""
    index = max(0, min(len(HANGMAN_PICS) - 1, 6 - tries))
    print(HANGMAN_PICS[index])


def get_letter_guess():
    """Get a valid single-letter guess from the player."""
    while True:
        guess = input("\nPlease guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess

        input("Invalid input. Please enter a single letter.")
        clear_screen()


def update_display(guess, word, display):
    """Reveal all matching letters in the hidden word."""
    for index, letter in enumerate(word):
        if letter == guess:
            display[index] = guess


def show_end_game_message(won, word):
    """Show a win or loss message at the end of the game."""
    if won:
        print(f"""
The word was '{word}'. Congratulations, you guessed it right!
        ================
        === You Win! ===
        ================
        """)
    else:
        print(f"\nThe word was \"{word}\". Better luck next time!")

    input("Press [Enter] to continue.")


def main():
    """Run the hangman game loop."""
    while True:
        show_instructions()
        difficulty = select_difficulty()
        word = get_random_word(difficulty)
        display = ["_"] * len(word)
        tries = 6
        already_guessed = []

        while "_" in display and tries > 0:
            clear_screen()
            display_hangman(tries)
            print(f"The word is: {' '.join(display)}")
            print(f"You have {tries} tries left.")
            print(f"Already guessed letters: {', '.join(already_guessed)}")

            guess = get_letter_guess()
            if guess in already_guessed:
                input("You already guessed that letter. Try again.")
            else:
                already_guessed.append(guess)
                if guess in word:
                    input("Nice guess!")
                    update_display(guess, word, display)
                else:
                    tries -= 1
                    input("Nope, try again.")

        show_end_game_message("_" not in display, word)

        if input("Do you want to play again? (y/N): ").lower() not in ["y", "yes"]:
            break


if __name__ == "__main__":
    main()
