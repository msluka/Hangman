# Hangman
import random

from hangman_drawings import stages
from word_list import word_list

lives = 6

chosen_word = random.choice(word_list)
chosen_word = chosen_word.lower()

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder+= "_"

print(placeholder)

game_over = False
correct_letters = []
used_letters = []

while not game_over:

    unique_used_letters = list(set(used_letters))
    print(unique_used_letters)

    guess = input("Guess a letter: ").lower()
    used_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives-=1
        if lives == 0:
            game_over = True
            print("You lose!")
            print(f"The word you failed to guess was: {chosen_word}")

        print(f"The letter is not in the word. You have {lives} tries left.")
        print(stages[lives])
    else:
        print(f"Congratulations! The letter is in the word.")

    print(display)
    if "_" not in display:
        game_over = True
        print("You won!")