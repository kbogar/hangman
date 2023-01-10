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


main_hangman(words_list)

