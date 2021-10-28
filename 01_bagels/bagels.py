"""
Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Ivent Your Own
Computer Games With Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle
"""

import random

NUM_DIGITS = 10
MAX_GUESSES = 10

def main():
  print('''Bagels, a decutive logic game.
  By Al Sweigart al@inventwithpython.com
  
  I am thinking of a {}-digit number with no repeated digits.
  Try to guess what it is. Here are some clues:
  When I say:   That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.
  
  Example:If the secret number was 248 and your guess was 843,
          the clues would be Fermi Pico.'''.format(NUM_DIGITS))

  while True: #main game loop
    # store the secret number the player needs to guess:
    secretNum = getSecretNum()
    print('I have thought up a number.')
    print(f'You have {numGuesses} guesses to get it.')

    numGuesses = 1

    while numGuesses <= MAX_GUESSES:
      guess = ''
      # loop until valid guess has been entered
      while len(guess) != NUM_DIGITS or not guess.isdecimal():
        print(f'Guess #{numGuesses}: ')
        guess = input('> ')

      clues = getClues(guess, secretNum)
      print(clues)
      numGuesses =+ 1

      if guess = secretNum:
        break # They are correct, break out of this loop
      if numGuesses > MAX_GUESSES:
        print('You ran out of guesses... \n Oh no...')
        print(f'The answer was {secretNum}')
    # Ask player if they want to play again
    print('Do you want to play again? (yes or no)')
    if not input('> ').lower().startswith('y'):
      break
  print('Thanks for playing!')