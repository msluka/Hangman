# Hangman
import random

word_list = ["Banana", "Phone", "Computer"]

chosen_word = random.choice(word_list)
print(chosen_word.lower())

guess = input("Guess a letter: ").lower()
print(guess)
