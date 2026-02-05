"""Bagels
A deductive logic game where you must guess a number based on clues
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def generateSecretNumber():
    """Return a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_Num = ''
    for i in range(NUM_DIGITS):
        secret_Num += str(numbers[i])
    return secret_Num


def getClues(guess, secret_number):
    """Return a string with the pico, fermi, bagels clue for a guess and secret number pair"""
    if guess == secret_number:
        return 'You got it!'

    clues = []
    # Need to check correctness and positions of guess to secret number
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            # Correct Digit in the right place
            clues.append('Fermi')
        elif guess[i] in secret_number:
            # Correct Digit in the wrong place
            clues.append('Pico')

    if len(clues) == 0:
        # No Correct digits
        return 'Bagels'
    else:
        # Sort clues into alphabetical order so original order doesn't give information away
        # User doesn't know which is correct or incorrect and return single string
        clues.sort()
        return ''.join(clues)


def gameLoop():
    while True:
        secret_number = generateSecretNumber()
        num_of_guesses = 1
        print('Guess {} of {}'.format(num_of_guesses, MAX_GUESSES))
        while num_of_guesses <= MAX_GUESSES:
            guess = ''
            # Conditions for valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(num_of_guesses))
                guess = input('> ')

            clues = getClues(guess, secret_number)
            print(clues)
            num_of_guesses += 1

            if guess == secret_number:
                break
            if num_of_guesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The secret number was: {}'.format(secret_number))

        play_again = input("Do you want to play again?  (YES or NO)\n>")
        if not play_again.lower().startswith('y'):
            break
    print('Thank you for playing!')


def main():
    print('''Bagels, a deductive logic game.
    By Sobelema Atemie

    I am thinking of a {}-digit number. Try to guess what it is.
    Here are some clues:
    When I say: That means:
    Pico        One digit is correct but in the wrong position
    Fermi       One digit is correct but in the right position
    Bagels      No digit is correct

    I have though up a number.
    You have {} guesses to get it
          '''.format(NUM_DIGITS, MAX_GUESSES))

    gameLoop()


if __name__ == '__main__':
    main()
