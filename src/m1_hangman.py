"""
Hangman.

Authors: Nathalie Grier and Lara Peters.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random

word = ''
guesses = []

def main():

    word = get_word()
    guesses.clear()
    dashes = str('-' * (len(word)))
    print('Here is your secret word:', dashes)
    num = get_difficulty()
    guess = get_guess()
    trials(guess, num, dashes, word)

def get_word():

    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()

    r = random.randrange(0, len(words))
    item = words[r]
    return item

def get_guess():

    x = str(input('Please guess a single letter: '))
    return x

def get_difficulty():

    a = int(input('How many unsuccessful choices do you want to allow yourself?: '))
    return a

def correct(num, word):

    dashes = ''
    for c in word:
        if c in guesses:
            dashes = dashes + c
        else:
            dashes = dashes + '-'

    if dashes == word:
        print('Congratulations, you won! Your secret word was: ', word)
        try_again()
    else:
        print('Good guess! You still have', num,
             'unsuccessful guesses left before you LOSE! Here is what you currently know about the secret word:')
        print(dashes)
        new = get_guess()
        trials(new, num, dashes, word)

def incorrect(dashes, num, guess, word):

    num = num - 1
    if num > 0:
        print('Sorry, there are no letters', guess,
              'in the secret word. Here is what you currently know about the word: ')
        print(dashes)
        print('You still have', num, 'unsuccessful guesses left.', )
        new = get_guess()
        trials(new, num, dashes, word)
    else:
        print('Sorry, you lost.')
        print('Your secret word was: ', word)
        try_again()

def trials(guess, num, dashes, word):

    k = 0
    while True:
        if k > len(word) - 1:
            print()
            incorrect(dashes, num, guess, word)
            break
        if guess == word[k]:
            print()
            guesses.append(guess)
            correct(num, word)
            break
        k = k + 1

def try_again():

    x = int(input('Do you want to play again? Type 1 for yes, type 2 for no: '))
    if x == 1:
        print()
        main()
    else:
        print()
        print('Thanks for playing, goodbye!')

main()