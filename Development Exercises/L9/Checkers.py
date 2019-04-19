# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A01223463, A00354776 
# Author: Bruno Vergaray, Alex Garcia
# Excercise: L9
# File name: Checkers.py
# Description: Checkers Game
# Date created: 04/07/2019
# Date last modified: 04/07/2019
# Python Version:  3.7.2

# Begin code
# amo a ver si sale esto

import random

#CONSTANTS SECTION
#White pawn
WP = "W"
#White queen
WQ = "£"
#Empty cell
EC = " "
#Black pawn
BP = "B"
#Black Queen
BQ = "$"
#END OF CONSTANTS SECTION

def init_grid():
    #Initialize the new game grid
    grid = [EC, WP, EC, WP, EC, WP, EC, WP,
            WP, EC, WP, EC, WP, EC, WP, EC,
            EC, WP, EC, WP, EC, WP, EC, WP,
            EC, EC, EC, EC, EC, EC, EC, EC,
            EC, EC, EC, EC, EC, EC, EC, EC,
            BP, EC, BP, EC, BP, EC, BP, EC,
            EC, BP, EC, BP, EC, BP, EC, BP,
            BP, EC, BP, EC, BP, EC, BP, EC]
    return grid

def drawBoard(board):
# This function prints out the board that it was passed.
# "board" is a list of 10 strings representing the board (ignore index)
    print('| '+board[56]+ ' | ' + board[57]+ ' | ' + board[58]+ ' | ' + board[59]+ ' | ' + board[60]+ ' | ' + board[61]+ ' | ' + board[62]+ ' | ' + board[63] + ' | ')
    print('| '+board[48]+ ' | ' + board[49]+ ' | ' + board[50]+ ' | ' + board[51]+ ' | ' + board[52]+ ' | ' + board[53]+ ' | ' + board[54]+ ' | ' + board[55] + ' | ')
    print('| '+board[40]+ ' | ' + board[41]+ ' | ' + board[42]+ ' | ' + board[43]+ ' | ' + board[44]+ ' | ' + board[45]+ ' | ' + board[46]+ ' | ' + board[47] + ' | ')
    print('| '+board[32]+ ' | ' + board[33]+ ' | ' + board[34]+ ' | ' + board[35]+ ' | ' + board[36]+ ' | ' + board[37]+ ' | ' + board[38]+ ' | ' + board[39] + ' | ')
    print('| '+board[24]+ ' | ' + board[25]+ ' | ' + board[26]+ ' | ' + board[27]+ ' | ' + board[28]+ ' | ' + board[29]+ ' | ' + board[30]+ ' | ' + board[31] + ' | ')
    print('| '+board[16]+ ' | ' + board[17]+ ' | ' + board[18]+ ' | ' + board[19]+ ' | ' + board[20]+ ' | ' + board[21]+ ' | ' + board[22]+ ' | ' + board[23] + ' | ')
    print('| '+board[8]+ ' | ' + board[9]+ ' | ' + board[10]+ ' | ' + board[11]+ ' | ' + board[12]+ ' | ' + board[13]+ ' | ' + board[14]+ ' | ' + board[15] + ' | ')
    print('| '+board[0]+ ' | ' + board[1]+ ' | ' + board[2]+ ' | ' + board[3]+ ' | ' + board[4]+ ' | ' + board[5]+ ' | ' + board[6]+ ' | ' + board[7] + ' | ')


def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player’s letter as the first item, and the
    # computer's letter as the second.
    letter = ''
    if not (letter == 'X' or letter == 'O'):
        print('Do you want to be Blacks or Whites? (B or W)')
    letter = input().upper()

    # the first element in the list is the player’s letter, the second is
    # computer's letter.
    if letter == 'B':
        return ['░', '▓']
    else:
        return ['▓', '░']


def turn(v):
    #Lleva el control de quien tenga el turno

    if v == True:
        return 'whites'
    else:
        return 'blacks'

# def whoGoesFirst():
#     # Randomly choose the player who goes first.
#     if random.randint(0, 1) == 0:
#         return 'computer'
#     else:
#         return 'player'
def playAgain():
    #This function returns True if the player wants to play again, otherwise it returns False
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board,letter,move):
    board[move] = letter

def isWinner(bo):
    #Given a board and a player's letter, this function returns True if that player has won.
    #We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[56] == " " and bo[57] == " " and bo[58] == " " and bo[59] == " " and bo[60] == " " and bo[61] == " " and bo[62] == " " and bo[63] == " ") or  # across the top
           (bo[48] == " " and bo[49] == " " and bo[50] == " " and bo[51] == " " and bo[52] == " " and bo[53] == " " and bo[54] == " " and bo[55] == " ") or # across the middle
           (bo[40] == " " and bo[41] == " " and bo[42] == " " and bo[43] == " " and bo[44] == " " and bo[45] == " " and bo[46] == " " and bo[47] == " ") or  # across the bottom
           (bo[32] == " " and bo[33] == " " and bo[34] == " " and bo[35] == " " and bo[36] == " " and bo[37] == " " and bo[38] == " " and bo[39] == " ") or  # down the left side
           (bo[24] == " " and bo[25] == " " and bo[26] == " " and bo[27] == " " and bo[28] == " " and bo[29] == " " and bo[30] == " " and bo[31] == " ") or  # down the middle
           (bo[16] == " " and bo[17] == " " and bo[18] == " " and bo[19] == " " and bo[20] == " " and bo[21] == " " and bo[22] == " " and bo[23] == " ") or  # down the right side
           (bo[8] == " " and bo[9] == " " and bo[10] == " " and bo[11] == " " and bo[12] == " " and bo[13] == " " and bo[14] == " " and bo[15] == " ") or  # diagonal
           (bo[0] == " " and bo[1] == " " and bo[2] == " " and bo[3] == " " and bo[4] == " " and bo[5] == " " and bo[6] == " " and bo[7] == " "))  # diagonal
def getBoardCopy(board):
    #Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    #Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in their move
    move = ' '
    box = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63'
    while move not in box.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    #Returns a valid move from the passed list on the passed board.
    #Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #Here is our algorithm for our checkers AI:
    #First, check if we can win in the next move

    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy):
                return i

    #Check if the player could win on their next move, and block them.

    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy,playerLetter, i)
            if isWinner(copy):
                return i



print('Welcome to Py-Checkers!')

while True:

    playerLetter, computerLetter = inputPlayerLetter()
    board = init_grid()
    theBoard = drawBoard(board)
    v = True

    while 1:
        if turn(v) == 'whites':
            print ('The ' + turn(v) + ' will go first.')
            break
        if turn(v) == 'blacks':
            print ('The ' + turn(v) + ' will go first.')
            break
