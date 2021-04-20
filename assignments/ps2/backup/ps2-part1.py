import string

def is_word_guessed(secret_word, letters_guessed):
    for letter in list(secret_word):
        if letter not in letters_guessed:
            return False
    return True

secret_word = 'apple'
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
print(is_word_guessed(secret_word, letters_guessed) )

secret_word = 'apple'
letters_guessed = ['a', 'l', 'p', 'p', 'e', 's']
print(is_word_guessed(secret_word, letters_guessed) )

def get_guessed_word(secret_word, letters_guessed):
    current_guess = ''
    for letter in list(secret_word):
        if letter in letters_guessed:
            current_guess += letter
        else:
            current_guess += '_ '

    return current_guess

secret_word = 'apple'
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
print(get_guessed_word(secret_word, letters_guessed))

def get_available_letters(letters_guessed):
    not_guessed = ''
##    for letter in 'abcdefghijklmnopqrstuvwxyz':
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            not_guessed += letter
    return not_guessed

letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
print(get_available_letters(letters_guessed))
