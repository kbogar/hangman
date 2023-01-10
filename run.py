# Importing libraries
import random
import string
# Imports from other files
from words import words_list
from hangmans import hangman_stages

#
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
    abc = set(string.ascii_uppercase)
    # Empty set of used letters to add them later
    used_letters = set()

    lives_left = 7
    # Inputs from user
    while len(letters_from_words) > 0 and lives_left > 0:
        print(f'You have {lives_left} lives left.')
        print('Used letters: ', ' '.join(used_letters))

        # Writes out the played letters that in used letters
        # or we write out '-'
        # prints out the hangman stages with lives left
        listwd = [letter if letter in used_letters else '-' for letter in word]
        print(hangman_stages[lives_left])
        print('Current word: ', ' '.join(listwd))


main_hangman(words_list)

