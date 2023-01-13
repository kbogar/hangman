"""
Import libraries random for selecting random
words for the game, and string module for
ASCII letters. Also imports from words.py and
hangmans.py.
"""
import random
import string
from words import words_list
from hangmans import hangman_stages


def welcome():
    """
    Start of the game with logo from (https://ascii.co.uk/art/hangman)
    a welcome message and game rules. Requests player name and prints
    out the corresponding message.
    """
    print(' _ ')                                            
    print('| |')                                            
    print('| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __')  
    print('|  _ \ / _  |  _ \ / _` |  _ ` _ \ / _` |  _ \ ') 
    print('| | | | (_| | | | | (_| | | | | | | (_| | | | |')
    print('|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|')
    print('                    __/ |        ')
    print('                   |___/    \n')
    print('************ Welcome to the Game! ************\n')
    print('This is a simple word guessing game. You have to')
    print('figure out an unknown word by guessing letters.')
    print('If too many letters which do not appear in the')
    print('word are guessed, then you are hanged and lose.\n')
    
    while True:
        global player_name
        player_name = input('Please enter your name: \n').upper()

        if player_name.isalpha() is not True:
            print('Your name must be alphabetic only.')
        else:
            print(f'Hello, {player_name}\n')
            break


def get_word(words_list):
    """
    This function checks if the word is correct or not
    and gets a random word with uppercase
    """
    word = random.choice(words_list)
    while ('-' in word) or (' ' in word):
        word = random.choice(words_list)

    return word.upper()


def play_again():
    """
    If the game is finished, the game asks the player if
    they wish to play again or not. If yes the game restarts,
    if not the game exit.
    """
    replay = input('Would you like to play again? Enter Y or N \n')
    if replay == 'y':
        main()
    else:
        print('Thank you for playing! Hope to see you soon!')


def start_hangman():
    """
    Main logic of the game play. It will get a word, 
    generate letters, it will ask player inputs,
    also check the lives left and generate 
    corresponding print statements.
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
        print(f'You have {lives_left} lives left.\n')
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
                print('Correct!\n')
            else:
                lives_left = lives_left - 1
                print('This letter is not in the word.\n')
                print('You lose a life.\n')
        elif played_letter in used_letters:
            print('You already guessed this letter. Please try again!\n')
        else:
            print('You can only guess one letter in alphabet.\n')
            print('Please try again!\n')
    # End game statements if player lose or win
    if lives_left == 0:
        print(hangman_stages[lives_left])
        print(f'I am sorry {player_name}, You lose! The word was {word}')
        play_again()
    else:
        print(f'Nice play {player_name}, you got the correct word: {word}')
        play_again()


def main():
    """
    Main functions of the game
    """
    welcome()
    start_hangman()


main()
