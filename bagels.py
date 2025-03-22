import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def generateSecretNumber():
    pass

def gameLoop():
    while True:
        secret_number = generateSecretNumber()
        num_of_guesses = 1
        print(f'Guess {num_of_guesses}')

        play_again = input("Do you want to play again?  (YES or NO")
        if not play_again.lower().startswith('y'):
            break

def main():
    print('''Bagels, a deductive logic game.
    By Sobelema Atemie
    
    I am thinking of a {}-digit number. Try to guess what it is.
    Here are some clues:
    When I say: That means:
    Pico        One digit is correct but in the wrong position
    Fermi       One digit is correct but in the wrong position
    Bagels      No digit is correct
    
    I have though up a number.
    You have {} guesses to get it
          '''.format(NUM_DIGITS,MAX_GUESSES))

    gameLoop()

if __name__ == '__main__':
    main()