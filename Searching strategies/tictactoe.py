"""
This project implements Tic-Tac-Toe as a deterministic,
zero-sum, perfect-information environment.
The objective is to explore later adversarial search algorithms,
beginning with Minimax and later Alpha-Beta pruning.

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

        #input validation
        while True:
            try:
                response = input("Player 1 enter your symbol and pick a number between 0 and 1."
                                                  "For example : X,0").split(',')
                self.player1 = response[0]
                decider1 = response[1]
                break
            except Exception as e:
                print("invalid input")


        num_format = re.compile(r'^[0-1]$')

        while not num_format.match(decider1):
            response1 = input("Player 1 enter your symbol and pick a number between 0 and 1."
                              "For example : X,0").split(',')
            if num_format.match(response1[1]):
                decider1 = response1[1]
                break
        decider1=int(decider1)
        self.player2 = input("Player 2 enter your symbol")
        if decider1==0:
            decider2=1
        else:
            decider2=0
        self.identities[decider1]=self.player1
        self.identities[decider2]=self.player2

        #Game starting by picking randomly a starter between the two players.
        #This is the reason behind the existence of the decider variable.
        #Player is identified by its symbols during the game.
        #Input validation to make sure the player does not make mistakes
        who_start= randint(0,1)
        row = 0
        column = 0
        while not self.game_over():
            print('Player recognizing by',str(self.identities[who_start]),"enter your location in the form : row,column separated by a comma")
            try:
                #Input validation
                player_input =input().split(',')
            except Exception as e:
                print("Invalid input")

            if len(player_input)!=2:
                continue
            try:
                row, column = map(int, player_input)
            except Exception as e:
                print("Enter value in the format symbol,number separated by a comma")
                continue
            num_format1 = re.compile(r'^[0-2]$')
            if not num_format1.match(str(row)) or not num_format1.match(str(column)):
                continue
            else:
                if self.grid[row][column] != " ":
                    print('occupied cell')
                    continue
                self.grid[row][column] = self.identities[who_start]
                for row in self.grid:
                    print(row)
                if self.game_over():
                    print('game over')
                    winner = self.winner_identity()
                    if winner==self.player1:
                        print('Player 1 wins')
                    elif winner==self.player2:
                        print('Player 2 wins')
                    else:
                        print('tie')
                    break
                who_start = 1 - who_start #swicth between the two players throughout the game


    def game_over(self):
        '''
        Check if the game is over
        :return: bool
        '''
        size = len(self.grid)
        if self.winner_identity() is not None:
            return True
        elif all(cell != " " for row in self.grid for cell in row):
            return True
        return False

    def winner_identity(self):
        '''
        Return the winner of the game
        :return: str or None
        '''
        size = len(self.grid)
        #Horizontal and vertical checking
        for i in range(size):
            if (self.grid[i][0] == self.player1 and self.grid[i][1] == self.player1 and self.grid[i][2] == self.player1):
                return self.player1
            elif (self.grid[i][0] == self.player2 and self.grid[i][1] == self.player2 and self.grid [i][2] == self.player2):
                return self.player2
            if (self.grid[0][i] == self.player1 and self.grid[1][i] == self.player1 and self.grid [2][i] == self.player1):
                return self.player1
            elif (self.grid[0][i]== self.player2 and self.grid[1][i] == self.player2 and self.grid [2][i] == self.player2):
                return self.player2

        #diagonals checking
        diag1 = []
        for i in range(1):
            for j in range(0, len(self.grid) - i):
                diag1.append(self.grid[i + j][j])

        if all(value == self.player1 for value in diag1):
            return self.player1
        elif all(value == self.player2 for value in diag1):
            return self.player2
        elif all(self.grid[i][size-1-i] == self.player1 for i in range(size)):
            return self.player1
        elif all(self.grid[i][size-1-i] == self.player2 for i in range(size)):
            return self.player2
        return None

#Test
grid = GRID() #instanciate the grid object to benefits from the methods
grid.build_grid() # build the grid as a 2D array
grid = grid.get_grid() #retrieve the grid

game = tictactoe(grid) #instanciate the tictactoe object to start the game related to the grid
game.game()