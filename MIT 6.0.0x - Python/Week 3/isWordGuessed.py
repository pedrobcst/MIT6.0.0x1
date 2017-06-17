# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 09:17:53 2017

@author: pedro
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for ch in secretWord:
        if(ch in lettersGuessed):
            correct = True
        else:
            return False
    return correct