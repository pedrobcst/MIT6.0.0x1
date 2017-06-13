# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 18:06:12 2017

@author: pedro_2
"""
# Paste your code into this box
up = 100
low = 0
guess = (up+low)/2

print("Please think of number between 0 and 100!")
while True:
    guess =(up+low)//2
    print("Is your secret number", guess, "?")
    com = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if(com == 'l'):
        low = guess
    elif(com == 'h'):
        up = guess
    elif(com == 'c'):
        print("Game over. Your secret number was:", guess)
        break
    else:
        print("Please input a correct command")

print