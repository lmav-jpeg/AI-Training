"""
Tic Tac Toe Implementation Human versus Human
Upcoming AI versus human
@author Laurie MAVOUNGOU lmavoungou@outlook.be
"""
from grid import GRID
from random import randint
import re
class tictactoe:
    '''
    Constructor
    '''
    def __init__(self, grid:'GRID'):
        self.grid = grid
        self.player1=None
        self.player2=None
        self.identities={}

    def game(self):
        '''
        Game logic
        :return: None
        '''
        response = input("Player 1 enter your symbol and pick a number between 0 and 1."
                                              "For example : X,0").split(',')
        self.player1 = response[0]
        num_format = re.compile(r'^[0-1]$')
        decider1 = response[1]
        while not num_format.match(decider1):
            response1 = input("Player 1 enter your symbol and pick a number between 0 and 1."
                              "For example : X,0").split(',')
            if not num_format.match(decider1):
                decider1 = int(response[1])
                break
        decider1=int(decider1)
        self.player2 = input("Player 2 enter your symbol")
        if decider1==0:
            decider2=1
        else:
            decider2=0
        self.identities[decider1]=self.player1
        self.identities[decider2]=self.player2

        who_start= randint(0,1)
        row = 0
        column = 0
        while not self.game_over():
            print('player recognizing by',str(self.identities[who_start]),"enter your location in the form row,column")
            row,column = map(int, input().split(','))
            num_format1 = re.compile(r'^[0-2]$')
            if not num_format1.match(str(row)) or not num_format1.match(str(column)):
                print('player recognizing by', str(self.identities[who_start]),
                      "enter your location in the form row,column")
            else:
                if self.grid[row][column] != " ":
                    print('occupied cell')
                    continue
                self.grid[row][column] = self.identities[who_start]
                for row in self.grid:
                    print(row)
                if self.game_over():
                    print('game over')
                    if all(self.grid[i][i] == self.player1 for i in range(len(self.grid))):
                        print('player 1 wins')
                    else:
                        print('player 2 wins')
                    break
                who_start = 1 - who_start


    def game_over(self):
        '''
        Check if the game is over
        :return: bool
        '''
        size = len(self.grid)
        for i in range(size):
            if (self.grid[i][0] == self.player1 and self.grid[i][1] == self.player1 and self.grid[i][2] == self.player1) or (self.grid[i][0] == self.player2 and self.grid[i][1] == self.player2 and self.grid [i][2] == self.player2):
                return True
            if (self.grid[0][i] == self.player1 and self.grid[1][i] == self.player1 and self.grid [2][i] == self.player1) or (self.grid[0][i]== self.player2 and self.grid[1][i] == self.player2 and self.grid [2][i] == self.player2):
                return True

        diag1 = []
        for i in range(1):
            for j in range(0, len(self.grid) - i):
                diag1.append(self.grid[i + j][j])

        if all(value == self.player1 for value in diag1) or all(value == self.player2 for value in diag1):
            return True
        elif all(self.grid[i][size-1-i] == self.player1 for i in range(size)):
            return True

        elif all(self.grid[i][size-1-i] == self.player2 for i in range(size)):
            return True
        elif all(cell != " " for row in self.grid for cell in row):
            return True
        return False

    def player_identity(self):
        pass

#Test
grid = GRID()
grid.build_grid()
grid = grid.get_grid()

game = tictactoe(grid)
game.game()