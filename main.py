# Hangman
import random

lives = 6

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["Banana", "Phone", "Computer"]

chosen_word = random.choice(word_list)
chosen_word = chosen_word.lower()
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder+= "_"

print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    guess = input("Guess a letter: ").lower()

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
        print(f"The letter is not in the word. You have {lives} tries left.")
        print(stages[lives])
    else:
        print(f"Congratulations! The letter is in the word.")

    print(display)
    if "_" not in display:
        game_over = True
        print("You won!")