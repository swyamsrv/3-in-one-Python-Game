"""     Rock, Paper and  scissors   """

from random import randint


def name_RPS():

    """This function is used to take input name from the user..."""

    player_name_RPS = input("Enter your name->\n")  # Name of the user

    return player_name_RPS


def gameon():

    """ Function will ask you to continue the game or not, Only YES and NO!!"""

    while True:
        game_on = input("Do you wanna play\nEither Yes or No-")
        if game_on[0].lower() == 'y':
            return True
        elif game_on[0].lower() == 'n':
            return False
        else:
            print("\nPlease Enter a Valid Input\n")
            continue


def choice_RPS():

    """This function indirectly takes the input, which was received by the computer """

    choose_RPS = randint(0, 2)
    comp = ['Rock', 'Paper', 'Scissors']

    if choose_RPS == 0:
        return comp[choose_RPS]

    elif choose_RPS == 1:
        return comp[choose_RPS]

    elif choose_RPS == 2:
        return comp[choose_RPS]


def inp():

    """This function takes input either Rock, Paper or Scissors"""

    while True:
        insrt = ['Rock', 'Paper', 'Scissors']
        print("\nPress\nR for Rock\nP for Paper\nS for Scissors\n")
        position = input()
        if position == 'r' or position == 'R':
            return insrt[0]
        elif position == 'p' or position == 'P':
            return insrt[1]
        elif position == 's' or position == 'S':
            return insrt[2]
        else:
            print("\nPlease Enter a valid Input\n")
            continue


"""MAIN"""


def r_p_s():
    """This function contains logic used to build Rock, Paper and Scissors Game"""
    while True:

        print("Hello, {}\nWelcome in this game.\n".format(name_RPS()))

        while gameon():
            comp_input = choice_RPS()
            win = inp()
            if win == comp_input:  # GAME WAS A TIE
                print("Computer = {}\n".format(comp_input))
                print("Play again\n")
                continue

            elif comp_input == 'Rock':  # ROCK
                if win == 'Rock':  # GAME WAS A TIE
                    print("Computer = {}\n".format(comp_input))
                    print("Play Again\n")
                    continue
                elif win == 'Paper':
                    print("Computer = {}\n".format(comp_input))
                    print("Congratulation! You Won.\n")
                    continue
                elif win == 'Scissors':
                    print("Computer = {}\n".format(comp_input))
                    print("Sorry You Lost\n")
                    continue

            elif comp_input == 'Paper':  # PAPER
                if win == 'Paper':   # GAME WAS A TIE
                    print("Computer = {}\n".format(comp_input))
                    print("Play Again\n")
                    continue
                elif win == 'Scissors':
                    print("Computer = {}\n".format(comp_input))
                    print("Congratulation! You Won.\n")
                    continue
                elif win == 'Rock':
                    print("Computer = {}\n".format(comp_input))
                    print("Sorry You Lost\n")
                    continue

            elif comp_input == 'Scissors':  # Scissors
                if win == 'Scissors':   # GAME WAS A TIE
                    print("Computer = {}\n".format(comp_input))
                    print("Play Again\n")
                    continue
                elif win == 'Rock':
                    print("Computer = {}".format(comp_input))
                    print("Congratulation! You Won\n")
                    continue
                elif win == 'Paper':
                    print("Computer = {}".format(comp_input))
                    print("Sorry You Lost")
                    gameon()

        print("Thank You playing....\n")
        break


"""END OF ROCK PAPER AND SCISSOR GAME!!"""

# _____________________________________________________________________________________________________________________

""" WORD GUESSING GAME """

import random

# library that we use in order to choose
# random words from a list of words

def word_guess():

    """Word guessing game!!"""

    print("Hello, Welcome to Word Guessing Game...\n")
    name_guess = input("What is your name?\n")
    # Here the user is asked to enter the name !!!!

    print("Good Luck ! ", name_guess)

    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'technical', 'fishing',
             'shadow', 'flashlight', 'ladder', 'birthday',
             'waterfall', 'measure', 'window', 'apartment', 'elephant',
             'basketball', 'cricket', 'penguin', 'scissors',
             'spoon', 'brave', 'dumbo', 'challenge', 'skateboard',
             'fishing', 'button', 'crown', 'player', 'blanket', 'shopping',
             'mirror', 'chocolate', 'engineering', 'signal', 'congratulations', 'swyam']

    # Function will choose one random
    # word from this list of words
    word = random.choice(words)

    print("Guess a characters\n")

    guesses = ''

    # Maximum of 10 turns will be given to tha user!!
    turns = 10

    while turns != 0:

        # counts the number of times a user fails
        failed = 0

        # all characters from the input
        # word taking one at a time.

        for char in word:

            # comparing that character with
            # the character in guesses
            if char in guesses:

                print(char)

            else:
                print("_")

                # for every failure 1 will be
                # incremented in failure
                failed += 1

        if failed == 0:
            # user will win the game if failure is 0
            # and 'You Win' will be given as output
            print("\nCongratulation!\nYou Won!!....")

            # this print the correct word
            print("\nThe word is-> ", word)
            break

        # if user has input the wrong alphabet then
        # it will ask user to enter another alphabet
        guess = input("\nGuess a character:\n")

        # every input character will be stored in guesses
        guesses += guess

        # check input with the character in word
        if guess not in word:

            turns -= 1

            # if the character does not match the word
            # then “Wrong” will be given as output
            print("Wrong")

            # this will print the number of
            # turns left for the user
            print("You have", + turns, 'more guesses\n')

            if turns == 0:
                print("You Lose\n")
                print("The word is-> {}\n".format(word))
    print("Thank You! for playing...\n")


"""END OF ROCK PAPER AND SCISSOR GAME!!"""

# ____________________________________________________________________________________________________________________


"""Tic-Tac-Toe"""


def O_OR_X(player1_name):
    """This function take's user input as 'X' or 'O' """

    print("{}!! please choose either 'X' or 'O'.\n".format(player1_name))
    player1 = ' '

    while player1 != 'X' or player1 != 'O':
        player1 = input("Enter 'X' for cross symbol and 'O' for circle symbol\n")
        if player1 == 'X':
            player2 = 'O'
            return player1, player2

        elif player1 == 'O':
            player2 = 'X'
            return player1, player2

        else:
            print("Please choose correct option")
            if player1 == 'x' or player1 == 'o':
                print("Please use upper case only \n")
            continue


def first_play(player1_name, player2_name):

    """ Function will decide who will start first!!! """

    print("Who will start {} or {} ?\nEnter 1 for {} and 2 for {}".format(player1_name, player2_name, player1_name,
                                                                          player2_name))

    while True:
        play = input()
        if int(play) == 1:
            return player1_name
        elif int(play) == 2:
            return player2_name
        else:
            print("Please Enter valid Input")
            print("Enter only 1 or 2")
            continue


def sample_board(sample):

    """This function displays the resultant board"""

    print("\nAvailable\n")

    print(sample[7], "|", sample[8], "|", sample[9])
    print("-" * 9)
    print(sample[4], "|", sample[5], "|", sample[6])
    print("-" * 9)
    print(sample[1], "|", sample[2], "|", sample[3])

    print("\n" * 2)


def display(board):
    """This function will provide a platform for the game after each and every step by the players"""

    print("Yours Board=>\n")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("-" * 9)
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("-" * 9)
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("\n")
    print("***************")


def index():

    """This function takes user input ,i.e. in which index does he want to place its 'X' or 'O'."""

    BOX = 0
    while BOX < 1 or BOX > 9:
        BOX = int(input("Enter a index position=>\n"))
        if BOX >= 1 and BOX <= 9:
            return BOX
        else:
            print("Invalid Input")
            print("Please! choose a correct index\n")
            continue


def place_marker(board, marker, position, sample):

    """This function is used for assigning the X or O in the board"""

    board[position] = marker
    sample[position] = " "


# place_marker(board, player1, position, sample)

def win_check(board, mark):

    """This function is used to check whether the person is winning or losing"""

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


# print(win_check(board, player1))

def space_check(board, position):

    """This function is to return whether any specific position is empty of not"""

    return board[position] == " "


def full_board_check(board):

    """This function is to check whether the board is full and returns a boolean true if full """

    for i in range(1, 10):
        if space_check(board, i):
            return False  # This will execute the space_check function if it returns True then board is not yet empty

    return True


def replay():

    """This function is to ask the user for proceeding for the game further"""

    rep = input("Do you want to play again?\nIf yes enter 'y', If No enter 'n'\n")
    while True:
        if rep[0].lower() == 'y':
            return True
        elif rep[0].lower() == 'n':
            return False
        else:
            print("Please Enter a valid Input\nYou can also type 'y' for YES and 'n' for NO\n")
            continue


"""MAIN"""


def tic_tac_toe():

    initial = 1
    while initial:

        print("Hello, Welcome to TIC-TAC-TOE!\n")

        player1_name = input("Enter the name of 1st player\n")
        player2_name = input("Enter the name of 2nd player\n")

        # WHILE LOOP TO KEEP THW GAME RUNNING !!!!

        while True:
            sample = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

            board = [" "] * 10

            player1, player2 = O_OR_X(player1_name)  # Assigning value to player either 'X' or 'O'..

            turn = first_play(player1_name, player2_name)  # Which player will play first

            print(turn + " will start the game \n")

            print("Are You Ready to play?")

            while True:
                play_game = input("Enter Yes or No\n")
                if play_game[0].lower() == 'y':
                    game_start = True
                    break
                elif play_game[0].lower() == 'n':
                    game_start = False
                    break
                else:
                    print("Please Enter a valid input\nYou can also Enter 'y' for YES and 'n' for NO\n")
                    continue

            while game_start:
                if turn == player1_name:
                    """1st Player's turn"""
                    sample_board(sample)  # Availability of free space

                    display(board)  # displaying the outcome on the board

                    print("\n{}'s Turn\nSign = {}".format(player1_name, player1))
                    position = index()  # Position of displaying 'X' or 'O'

                    place_marker(board, player1, position, sample)  # Will assign the value on the board

                    if win_check(board, player1):
                        display(board)
                        sample_board(sample)
                        print("Congratulation {}  won the game\n".format(player1_name))
                        game_start = False

                    else:
                        if full_board_check(board):
                            display(board)
                            sample_board(sample)
                            print("The Game is a draw!\n")
                            break
                        else:
                            turn = player2_name

                else:
                    """2nd Player's turn"""
                    sample_board(sample)  # Availability of free space

                    display(board)  # displaying the outcome on the board

                    print("\n{}'s Turn\nSign = {}".format(player2_name, player2))
                    position = index()  # Position of displaying 'X' or 'O'

                    place_marker(board, player2, position, sample)  # Will assign the value on the board

                    if win_check(board, player2):
                        display(board)
                        sample_board(sample)
                        print("Congratulation {} won the game\n".format(player2_name))
                        game_start = False
                    else:
                        if full_board_check(board):
                            display(board)
                            sample_board(sample)
                            print("The Game is a draw!\n")
                            break
                        else:
                            turn = player1_name

            if not replay():
                initial = 0
                break

        print("Thank You! for playing...")


""" MAIN CONTROL """

print("Hey! Buddy, Must be having a Wonderful day\nWelcome to the game\n\U0001f600")

while True:
    cond = input("1  ~  Rock-Paper & Scissors\n2  ~  Word Guessing Game\n3  ~  Tic-Tac-Toe\n\nEnter 0 to Quit\n")
    if cond.isnumeric():
        if int(cond) == 0:
            break

        if int(cond) == 1:
            r_p_s()   # ROCK PAPER AND SCISSOR
            continue

        elif int(cond) == 2:
            word_guess()  # WORD GUESSING GAME
            continue

        elif int(cond) == 3:
            tic_tac_toe()  # TIC-TAC-TOE
            continue

        else:
            print("Please Enter a Valid Input\n")
            continue
    else:
        print("Invalid Selection\n")
        continue
print("Thank you\nLife is Short, Play More")
