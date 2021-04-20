# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Echo Zhou
# Collaborators : <your collaborators>
# Time spent    : 3.5 hr

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word, 30 min
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters,
    or the empty string "". You may not assume that the string will only contain
    lowercase letters, so you will have to handle uppercase and mixed case strings
    appropriately.

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    wordlen = len(word)
    word = word.lower()
    letter_score = 0

    ## compute the letter score using the SCRABBLE_LETTER_VALUES dict for each letter
    for letter in word:
        letter_score += SCRABBLE_LETTER_VALUES.get(letter,0)

    ## compute the length_score according to the hand length and word length
    if (7 * wordlen - 3 * (n - wordlen) > 1):
        length_score =  7 * wordlen - 3 * (n - wordlen)
    else:
        length_score = 1

    ## total score
    return letter_score * length_score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    ## repeated print the letter according to the number in the dict
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4. 10mins
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand={}

    ## one of the letter replaced by '*'
    num_vowels = int(math.ceil(n / 3)) - 1

    ## one '*'
    hand['*'] = 1

    ## random choose vowels
    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    ## random choose consonants
    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters, 20 mins
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """

    ## copy the hand, avoid changing the original dict
    new_hand = hand.copy()
    ## convert all letters in word to lowercase
    word = word.lower()

    ## loop through all letters in word
    for letter in word:

        ## if the letter is in hand
        if letter in new_hand.keys():

            ## get the number in letter and deduct 1, default from .get() is 0
            new_hand[letter] = new_hand.get(letter, 0) - 1

            ## if 0 left in letter, remove the item from the dict
            if new_hand[letter] == 0:
                del new_hand[letter]

    return new_hand


#
# Problem #3: Test word validity, 5mins
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    word = word.lower()
    check_hand = hand.copy()

    ## if not in wordlist and not a '*' replaced word
    if word not in word_list and '*' not in word:
        return False

    ## deal with the exception of '*' word
    elif word not in word_list and '*' in word:

        ## construct possible words and check each of them against the wordlist
        for vowel in VOWELS:
            possible_word = word.replace('*', vowel)
            ## if any of the possible_word match in the word_list
            if possible_word in word_list:
                return True
        ## all possible_word does not work
        return False

    else:
        ## check if all the letter are in hand
        for letter in word:
            if letter not in check_hand.keys() and letter != '*':
                return False

            ## deduct the letter if the letter used in hand
            else:
                check_hand[letter] = check_hand.get(letter, 0) - 1
                if check_hand[letter] == 0:
                    del check_hand[letter]
    return True

#
# Problem #5: Playing a hand, 40 mins
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    handlen = 0
    for letter in hand.keys():
        handlen += hand[letter]

    return handlen


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """


    ## Initialize and keep track of the total score
    total_score = 0
    ## get the hand length
    n =  calculate_handlen(hand)

    ## As long as there are still letters left in the hand:
    while n > 0:

        ## Display the hand
        print("Current Hand:", end = ' ')
        display_hand(hand)

        ## Ask user for input
        word = input('Enter word, or "!!" to indicate that you are finished:')

        ## If the input is two exclamation points:
        if word == '!!':
            ## End the game (break out of the loop)
            break

        ## Otherwise (the input is not two exclamation points):
        else:
            ## If the word is valid:
            if is_valid_word(word, hand, word_list):

                ## Tell the user how many points the word earned,
                word_score = get_word_score(word, n)
                ## and the updated total score
                total_score += word_score
                print(f'"{word}" earned {word_score} points. Total: {total_score} points')

            ## Otherwise (the word is not valid):
            else:
                ## Reject invalid word (print a message)
                print("That is not a valid word. Please choose another word.")

            ## update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, word)
            n =  calculate_handlen(hand)

    if n == 0:
        print("Ran out of letters")

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    # print(f"Total score: {total_score} points")

    # Return the total score as result of function
    return total_score

# word_list = load_words()
# play_hand({'c':1, 'o': 1,  'w':1, 's': 1, '*': 1,  'z':1 }, word_list)
# play_hand({'a':1, 'j': 1,  'e':1, 'f': 1, '*': 1,  'r':1,  'x':1 }, word_list)
# play_hand({'a':1, 'c': 1,  'f':1, 'i': 1, '*': 1,  't':1,  'x':1 }, word_list)

#
# Problem #6: Playing a game, 1hr
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()

    ## loop until break (break condition: x not in hand)
    while True:
        if letter in VOWELS or letter == '*':
            x = random.choice(VOWELS)
        elif letter in CONSONANTS:
            x = random.choice(CONSONANTS)
        else:
            print("The input is not a valid letter")

        ## if the randomly chosen x is not in hand, replace letter and break
        if x not in new_hand.keys():
            ## replace letter by x
            new_hand[x] = new_hand[letter]
            ## delete letter
            del new_hand[letter]
            break

    return new_hand

# print(substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l'))



def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    ## initialize and keep total score
    total_score = 0

    ## start the game and get the num of hand from user
    num_hands = int(input("Enter total number of hands: "))

    ## 1 replay allowed
    num_replay = 1

    ## play num_hands
    for i in range(num_hands):

        ## start a hand
        hand = deal_hand(HAND_SIZE)

        print("Current Hand:", end = ' ')
        display_hand(hand)

        ## ask if need substitue letter, default as 'no'
        substitute = input("Would you like to substitute a letter?" or 'no')
        if substitute == 'yes':
            replace_letter = input('Which letter would you like to replace: ')
            hand = substitute_hand(hand, replace_letter)
            print()

        ## copy the hand to save for replay later
        replay_hand = hand.copy()
        ## play one hand and get the sccore
        total_score_hand = play_hand(hand, word_list)


        print("Total score for this hand: ", total_score_hand)
        print('----------')

        ## check for Replaying, if still left ask if the user want replay
        if num_replay > 0:
            replay = input('Would you like to replay the hand?' or 'no')
            if replay == 'yes':
                num_replay -= 1
                total_score_replay = play_hand(replay_hand, word_list)
                print("Total score for this hand: ", total_score_replay)
                print('----------')

                ## compare the replay score with before reply
                if total_score_replay > total_score_hand:
                    ## and store the largest as the hand score
                    total_score_hand = total_score_replay

        ## add the hand score to the total
        total_score += total_score_hand

    ## print the total score after completing all hands
    print("Total score over all hands: ", total_score)

    # print("play_game not implemented.") # TO DO... Remove this line when you implement this function



#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
