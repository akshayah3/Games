__author__ = 'Akshay'
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 18:57:17 2014

"""
import random

class Rps():
    """
    A simple game of rock papers and scissors.Rock-paper-scissors is a hand game usually played by two people,
    where players simultaneously form one of three shapes with an outstretched hand. The "rock" beats scissors,
     the "scissors" beat paper and the "paper" beats rock; if both players throw the same shape, the game is tied.

    """
    def __init__(self):
        values = ['rock', 'paper', 'scissors']
        player_values = raw_input('Show the shape of your fist')
        if player_values in values:
            computer_values = self.randomize(values)
            return self.result(player_values, computer_values)

    def replay(self):
        option = raw_input('Do you want to play again ? (y/n)')
        option = option.lower()
        if option == 'y':
            return self.__init__()
        elif option == 'n':
            pass
        else:
            print "enter y or n"
            self.replay()

    def randomize(self, computer_values):
        random.shuffle(computer_values)
        return computer_values[0]

    def result(self, player_value, computer_values):
        if player_value == computer_values:
            print "Draw"
            self.replay()
        else:
            if player_value == 'rock':
                if computer_values == 'paper':
                    print "You Lose, computer chose %s" % computer_values
                    self.replay()
                else:
                    print "You win computer chose %s" % computer_values
                    self.replay()
            elif player_value == 'paper':
                if computer_values == 'scissors':
                    print "You lose computer chose %s" % computer_values
                    self.replay()
                else:
                    print "You win computer chose %s" % computer_values
                    self.replay()
            elif player_value == 'rock':
                if computer_values == 'paper':
                    print "you lose computer chose %s" % computer_values
                    self.replay()
                else:
                    print "You win computer chose %s" % computer_values
                    self.replay()

a = Rps()
a.__init__
