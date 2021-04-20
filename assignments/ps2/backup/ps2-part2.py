import string

def is_word_guessed(secret_word, letters_guessed):
    for letter in list(secret_word):
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    current_guess = ''
    for letter in list(secret_word):
        if letter in letters_guessed:
            current_guess += letter
        else:
            current_guess += '_ '

    return current_guess

def get_available_letters(letters_guessed):
    not_guessed = ''
##    for letter in 'abcdefghijklmnopqrstuvwxyz':
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            not_guessed += letter
    return not_guessed

def hangman(secret_word):

    warnings = 3
    guesses = 6
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings} warnings left.")
    print("-------------")


    letters_guessed = []

    while guesses > 0:
        print(f"You have {guesses} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")

        letter_guessed = input("Please guess a letter: ").lower()


        if not letter_guessed.isalpha():
            print("Oops! That is not a valid letter. ")
            if warnings != 0:
                warnings -= 1
                print("You have ", warnings, "warnings left:")
                print(get_guessed_word(secret_word, letters_guessed), '\n------------')
            else:
                guesses -= 1
                print("You have no warnings left so you lose one guess:",\
                 get_guessed_word(secret_word, letters_guessed), '\n------------')


        elif letter_guessed in letters_guessed:
            print("Oops! You've already guessed that letter.")
            if warnings != 0:
                warnings -= 1
                print("You have ", warnings, "warnings left:")
                print(get_guessed_word(secret_word, letters_guessed), '\n------------')
            else:
                guesses -= 1
                print("You have no warnings left so you lose one guess:",\
                 get_guessed_word(secret_word, letters_guessed), '\n------------')


        else:
            letters_guessed.append(letter_guessed)

            if letter_guessed in secret_word:
                print("Good guess: ",\
                 get_guessed_word(secret_word, letters_guessed), '\n------------')
            else:
                print("Oops! That letter is not in my word: "
                , get_guessed_word(secret_word, letters_guessed), '\n------------')
                if letter_guessed in 'aeiou':
                    guesses -= 2
                else:
                    guesses -= 1

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

        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was", secret_word)


#hangman('tact')
hangman('else')
