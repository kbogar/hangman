# Importing libraries
import random
import string
# Imports from other files
from words import words_list
from hangmans import hangman_stages


def get_word(words_list):
    """
    This function checks if the word is correct or not
    and gets a random word with uppercase
    """
    word = random.choice(words_list)
    while ('-' in word) or (' ' in word):
        word = random.choice(words_list)

    return word.upper()


def main_hangman(words_list):
    """
    Main function for testing
    """
    word = get_word(words_list)
    # Variable to generate letters from words
    letters_from_words = set(word)
    # Return all Ascii letters in uppercase and store in variable
    alphabet = set(string.ascii_uppercase)
    # Empty set of used letters to add them later
    used_letters = set()

    lives_left = 7
    # Inputs from player
    while len(letters_from_words) > 0 and lives_left > 0:
        print(f'You have {lives_left} lives left.')
        print('Used letters: ', ' '.join(used_letters))

        # Writes out the played letters that in used letters
        # or we write out '-'
        # prints out the hangman stages with lives left
        # a b c - - -
        secret_word = [
            letter if letter in used_letters else '-' for letter in word]
        print(hangman_stages[lives_left])
        print('Current word: ', ' '.join(secret_word))
        # Ask player the next move
        # Checks if the played letter is in the word
        # Add or remove the played letter and remove the lives left
        played_letter = input('Guess the letter: ').upper()
        if played_letter in alphabet - used_letters:
            used_letters.add(played_letter)
            if played_letter in letters_from_words:
                letters_from_words.remove(played_letter)
            else:
                lives_left = lives_left - 1
                print('This letter is not in the word.')
        elif played_letter in used_letters:
            print('You already guessed this letter. Please try again!')
        else:
            print('Wrong input. Please try again!')
    # End game statements if player lose or win
    if lives_left == 0:
        print(hangman_stages[lives_left])
        print(f'I am sorry, You lose! The word was {word}')
    else:
        print(f'Nice play, you got the correct word: {word}')


main_hangman(words_list)