# Problem Set 2, hangman.py
# Name: Echo
# Collaborators:
# Time spent: part2: 2hrs + part3: 0.5hr

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    ## loop through all the letter in the secret word
    for letter in list(secret_word):
        ## if there is a letter not guessed in the secret word, return False
        if letter not in letters_guessed:
            return False

    ## if all the letter in secret word are in guessed, return True
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    current_guess = ''

    ## loop through the letters in secret word
    for letter in list(secret_word):

        ## if the letter is guessed, add the letter
        if letter in letters_guessed:
            current_guess += letter

        ## if the letter not guessed, replace by an underscore
        else:
            current_guess += '_ '

    ## return the string
    return current_guess


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    not_guessed = ''
    ##  for letter in 'abcdefghijklmnopqrstuvwxyz':
    for letter in string.ascii_lowercase:

        ## if the letter is not used, add to not_guessed
        if letter not in letters_guessed:
            not_guessed += letter

    ## return the string of all unused letters
    return not_guessed


def warning_message(warnings, guesses):
    '''
    calculate the warning, and guess number left,
    display the corresponding warning message
    '''
    ## if there is still warning left
    ## if warnings != 0:
    if warnings > 0:

        ## deduct 1 warning and print the the number of warnings left
        warnings -= 1
        print("You have ", warnings, "warnings left:", end = ' ')

    ## if no warning ledt, deduct 1 guess instead
    else:
        guesses -= 1
        print("You have no warnings left so you lose one guess:", end = ' ')

    ## return the tuple of warning and guess left
    return (warnings, guesses)



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    ## initialize the number of warnings and guesses
    warnings = 3
    guesses = 6

    ## print start message
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings} warnings left.")
    print("-------------")

    ## initialize the letter_guessed string
    letters_guessed = []

    ## if there are still guesses left
    while guesses > 0:

        ## Start the round
        print(f"You have {guesses} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")

        ## Take the input and convert it to a lower case character
        letter_guessed = input("Please guess a letter: ").lower()

        ## if the user did not enter a letter (instead ,a symbol or number), deduct one chance
        if not letter_guessed.isalpha():
            print("Oops! That is not a valid letter.", end = ' ')
            (warnings, guesses) = warning_message(warnings, guesses)

        ## check if the letter has already been guessed, deduct one chance
        elif letter_guessed in letters_guessed:
            print("Oops! You've already guessed that letter.", end = ' ')
            (warnings, guesses) = warning_message(warnings, guesses)

        ## if the input is a proper letter
        else:
            ## add the letter to the guessed letter list
            letters_guessed.append(letter_guessed)

            ## if the guessed letter is in the secret word
            if letter_guessed in secret_word:
                print("Good guess: ", end = ' ')

            ## if the letter not in the word
            else:
                print("Oops! That letter is not in my word: ", end = ' ')

                # deduct 2 guess if vowel, 1 guess if consonant
                if letter_guessed in 'aeiou':
                    guesses -= 2
                else:
                    guesses -= 1

            ## break out of the loop when the word is guessed
            if (is_word_guessed(secret_word, letters_guessed)):

                # calculate the number of unique letters in the word
                secret_word_unique = ''
                for letter in secret_word:
                    if letter not in secret_word_unique:
                        secret_word_unique += letter

                ## word guessed before the guess ran out, print the message and score
                print("Congratulations, you won!")
                print("Your total score for this game is:", \
                guesses * len(secret_word_unique))
                # score = guesses * len(secret_word.unique())
                break

        ## print the current guessed word
        print(get_guessed_word(secret_word, letters_guessed), '\n------------')

        ## if the loop end after guess ran out, print the message and the word
        if guesses <= 0:
            print("Sorry, you ran out of guesses. The word was", secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    ## remove the ' ' in ' _'
    my_word = my_word.replace(' ', '')

    ## if the length of the two words does not match, no match
    if len(my_word) != len(other_word):
        return False

    ## length match
    else:
        for index in range(len(other_word)):
            ## if the letter at same position does not match and is not a "_"
            if my_word[index] != '_' and my_word[index] != other_word[index]:
                return False

            ## if the char is '_', but this letter in other_word appear in my_word
            ## print(match_with_gaps("a_ ple", "apple")), should get false
            elif my_word[index] == '_' and other_word[index] in my_word:
                return False

    ## if all the exceptions did not return
    return True

# print(match_with_gaps("te_ t", "tact"))
# print(match_with_gaps("a_ _ le", "banana"))
# print(match_with_gaps("a_ _ le", "apple"))
# print(match_with_gaps("a_ ple", "apple"))


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    ## initiate the list for match words
    wordlist_match = []

    ## loop through the words in the list
    for word in wordlist:

        ## call the match function to compare, and append to possible word if match
        if (match_with_gaps(my_word, word)):
            wordlist_match.append(word)

    ## if not word in the match list
    if len(wordlist_match) == 0:
        print("No matches found")
    ## print the word match list as string
    else:
        print("Possible word matches are:")
        ## join the words to a string using ' '
        print(' '.join(wordlist_match))

# show_possible_matches("t_ _ t")
# show_possible_matches("abbbb_ ")
# show_possible_matches("a_ pl_ ")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''

    ## initialize
    warnings = 3
    guesses = 6

    ## start the game
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings} warnings left.")
    print("-------------")

    letters_guessed = []

    ## loop while guess left
    while guesses > 0:

        ## start the round
        print(f"You have {guesses} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")

        ## Take the input and convert it to a lower case character
        letter_guessed = input("Please guess a letter: ").lower()

        ## if the user did not enter a letter (instead ,a symbol or number)
        if not letter_guessed.isalpha():
            ## hint if required with '*'
            if letter_guessed == '*':
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That is not a valid letter.", end = ' ')
                (warnings, guesses) = warning_message(warnings, guesses)

        ## check if the letter has already been guessed
        elif letter_guessed in letters_guessed:
            print("Oops! You've already guessed that letter.", end = ' ')
            (warnings, guesses) = warning_message(warnings, guesses)

        else:
            ## add the letter to the guessed letter list
            letters_guessed.append(letter_guessed)

            if letter_guessed in secret_word:
                print("Good guess: ", end = ' ')
            else:
                print("Oops! That letter is not in my word: ", end = ' ')
                if letter_guessed in 'aeiou':
                    guesses -= 2
                else:
                    guesses -= 1

            ## break out of the loop when the word is guessed
            if (is_word_guessed(secret_word, letters_guessed)):
                secret_word_unique = ''
                for letter in secret_word:
                    if letter not in secret_word_unique:
                        secret_word_unique += letter

                print("Congratulations, you won!")
                print("Your total score for this game is:", \
                guesses * len(secret_word_unique))
                # score = guesses * len(secret_word.unique())
                break

        print(get_guessed_word(secret_word, letters_guessed), '\n------------')

        if guesses <= 0:
            print("Sorry, you ran out of guesses. The word was", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = "apple" #choose_word(wordlist)
    hangman_with_hints(secret_word)
