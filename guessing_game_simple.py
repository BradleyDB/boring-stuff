# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 11:11:32 2020

@author: bradl
"""


import random
#this block asks for the users name and sets up the premise of the game
print('Hey There, what is your name?')
name = input()
secret_Number = random.randint(1,25) #randomly sets the number to guess
print("Well, " + name +", I am thinking of a number between 2 and 17") #make sure this matches the previous line

#this block ellicits the users guess
for guesses_taken in range(1,5): #this range sets the number of guesses the user gets
    guess = input("Take a guess.\n")
    #the try block is for error handling if the user does not enter an int
    try:
        int_guess = int(guess)
        if type(int_guess) == int:
            #this if block is to tell the user if their guess is too high or too low
            if int_guess < secret_Number:
                print("Your Guess is too low")
            elif int_guess > secret_Number:
                print("Your guess it too high.")
            else:
                break
    except ValueError:
        print("Please enter in a numeral")   
if int_guess == secret_Number:
    if int(guesses_taken) > 1: #this tells the user how many guesses it gook to be correct
        print("Good job, " + name + "! You guessed my number in " + str(guesses_taken) + " guesses.")
    else: 
        print("Good job, " + name + "! You guessed my number on your first try!")
else: #tells the user what the number was if they did not guess correctly
    print("Nope. The number I was thinking of was " + str(secret_Number) + ".")
        
