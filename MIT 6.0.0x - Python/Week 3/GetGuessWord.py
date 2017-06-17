# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 08:18:23 2017

@author: pedro
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    resp = ''
    for ch in secretWord:
        if(ch in lettersGuessed):
            resp += ch
        else:
            resp += '_ '
    return resp   
