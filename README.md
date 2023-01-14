# HANGMAN
Hangman is a simple word guessing game, which runs in the mock terminal on Heroku. The player have to guess the secret word by inputing letters. If the letter is incorrect the hangman visuals will appear to the player with a remaining lives left. If the secret word is not solved after 7 guesses the player is lost the game. This retro terminal game will provide fun gaming time for the user. 

You can read more about the game on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)).

* Git Repository can be found here: https://github.com/kbogar/hangman

* Deployed game site can be found here: https://hangman024.herokuapp.com/

![](/assets/images/screenshot.png)

# FEATURES
## Existing features
* Welcome to the game with a game logo and a brief description of the rules.
* User name request

![](/assets/images/hangman1.png)

* Once the user enters his user name it starts the game with hello "Users Name".
* It shows the lives left, used letters, secret word to guess and guess the letter input from user.

![](/assets/images/hangman2.png)

* After the input from user, the terminal prints out which letter he guessed, if the letter is in the secret word or not
* You lose a life, lifes left, used letters, the first hangman visual because the letter was not correct
* Secret word currently empty and next imput from user to guess a letter.

![](/assets/images/hangman3.png)

* You already guessed this letter. Please try again! - message if the user already used the same letter.

![](/assets/images/hangman4.png)

* You can only guess one letter in alphabet. - message if the user inputs numbers or more then one letter.

![](/assets/images/hangman5.png)

* If the user guessed a correct letter, it prints out - Correct! to the terminal
* Add a letter to used letters and also to secret word. 

![](/assets/images/hangman6.png)

* Game Lost - if the user used all his lifes, it prints out the last hangman visual, lose message with the users name and unveil the secret word.
* Then the terminal prints out a question - Would you like to play again Y or N 
* The game waits for user input.

![](/assets/images/hangman7.png)

* If the user choose Y then the game restarts with a message - Nice! Have a try again User Name.

![](/assets/images/hangman8.png)

* If the user choose N then the game exits with a message - Thank you for playing! Hope to see you soon.

![](/assets/images/hangman9.png)

* Game Win - If the user guess the secret word and wins, the terminal prints out a congratulation message, unveiling the secret word.
* Then the terminal prints out a question - Would you like to play again Y or N
* The game waits for user input.

![](/assets/images/hangman10.png)