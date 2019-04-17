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
import random

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
