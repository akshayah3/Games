__author__ = 'Akshay'

class Tictactoe:
    """
    A simple game of Tictactoe
    """
    Fi = [None, None, None]
    Se = [None, None, None]
    Th = [None, None, None]
    structure = ['first', 'second', 'third']
    moves = ['o', 'x']
    playermoves = 0
    computermoves = 0
    def __init__(self):




    def player_move(self):
        row = raw_input('which row do you want to play?')
        if row in structure:
            if self.row_validation(row):
                column = raw_input('which column do you want to play?')
                if self.column_valdation(column):


    def computer_move(self):

    def row_validation(self, row):


    def column_valdation(self):



    def result(self):
