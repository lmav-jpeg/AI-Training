"""
This project implements Tic-Tac-Toe AI versus human as a deterministic,
zero-sum, perfect-information environment.
It mixes DFS and MINIMAX decision making to make the game AI unbeatable

@author Laurie MAVOUNGOU lmavoungou@outlook.be
@position CEO of JK AI
"""
from grid import GRID
from random import randint, choice
import re

class MINIMAX:
    '''
    Constructor
    '''
    def __init__(self, grid: 'GRID', player2_symbol: str):
        self.grid = grid
        self.player1 = "AI"
        self.player2 = player2_symbol
        self.track = {}
        self.last_neighbor = None
        self.identities = {}

    def game(self):
        '''
        Game logic
        :return: None
        '''
        decider1 = choice((0, 1))
        if decider1 == 0:
            decider2 = 1
        else:
            decider2 = 0
        self.identities[decider1] = self.player1
        self.identities[decider2] = self.player2

        who_start = randint(0, 1)

        while not self.game_over():
            row = 0
            column = 0
            try:
                if self.identities[who_start] == self.player1:
                    print("\nAI Turn!")
                    self.track = {}  # Clear previous moves tracking map
                    score, _ = self.minimaxDFS(swicth=True, depth=0)
                    row, column = self.best_move(score)
                    print(f"AI plays move: ({row}, {column})")
                else:
                    print(f'\nPlayer 2 ({self.player2}) Turn!',
                          "enter your location in the form : row,column separated by a comma")
                    player_input = input().split(',')
                    if len(player_input) != 2:
                        continue
                    row, column = map(int, player_input)
            except (ValueError, IndexError, TypeError):
                print("Invalid input or move selection error.")
                continue

            num_format1 = re.compile(r'^[0-2]$')
            if not num_format1.match(str(row)) or not num_format1.match(str(column)):
                print("Out of bounds range (0-2 required).")
                continue

            if self.grid[row][column] != " ":
                print('Occupied cell!')
                continue

            # Place move on the board
            self.grid[row][column] = self.identities[who_start]

            # Print updated board
            print("\nCurrent Board State:")
            for grid_row in self.grid:
                print(grid_row)

            if self.game_over():
                print('\nGame Over!')
                winner = self.winner_identity()
                if winner == self.player1:
                    print('AI Player wins!')
                elif winner == self.player2:
                    print('Player 2 wins!')
                else:
                    print('Tie!')
                break

            who_start = 1 - who_start  # Switch turns

    def minimaxDFS(self, neighbor=None, score=0, swicth=True, depth=0):
        '''
        Traversal of the MINIMAX-DFS algorithm.
        :return: (int, dict)
        '''
        if self.winner_identity() == self.player1:
            return 1, self.track
        elif self.winner_identity() == self.player2:
            return -1, self.track
        elif self.winner_identity() is None and self.game_over():
            return 0, self.track

        begin_neighbors = self.available_moves()
        if swicth:
            best_score = -float('inf')
            if begin_neighbors:
                #AI supposed Move
                for neighbor in begin_neighbors:
                    row, column = neighbor
                    self.grid[row][column] = "AI"
                    score, _ = self.minimaxDFS(neighbor, score, False, depth + 1)
                    self.grid[row][column] = " "  # Backtrack
                    if depth == 0:
                        self.track[neighbor] = score
                    best_score = max(score, best_score)

            return best_score, self.track
        else:
            #Human Supposed Move
            best_score = float('inf')
            if begin_neighbors:
                for neighbor in begin_neighbors:
                    row, column = neighbor
                    self.grid[row][column] = self.player2
                    score, _ = self.minimaxDFS(neighbor, score, True, depth + 1)
                    self.grid[row][column] = " "  # Backtrack
                    if depth == 0:
                        self.track[neighbor] = score
                    best_score = min(score, best_score)
            return best_score, self.track

    def best_move(self, best_score):
        for move, score in self.track.items():
            if score == best_score:
                return move
        return None

    def game_over(self):
        '''
        Check if the game is over
        :return: bool
        '''
        if self.winner_identity() is not None:
            return True
        return all(cell != " " for row in self.grid for cell in row)

    def winner_identity(self):
        '''
        Return the winner of the game
        :return: str or None
        '''
        size = len(self.grid)
        # Horizontal and Vertical checking
        for i in range(size):
            if (self.grid[i][0] == self.player1 and self.grid[i][1] == self.player1 and self.grid[i][2] == self.player1):
                return self.player1
            elif (self.grid[i][0] == self.player2 and self.grid[i][1] == self.player2 and self.grid[i][2] == self.player2):
                return self.player2
            if (self.grid[0][i] == self.player1 and self.grid[1][i] == self.player1 and self.grid[2][i] == self.player1):
                return self.player1
            elif (self.grid[0][i] == self.player2 and self.grid[1][i] == self.player2 and self.grid[2][i] == self.player2):
                return self.player2

        # Diagonals checking
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != " ":
            return self.grid[0][2]

        return None

    def available_moves(self):
        '''
        Returns available empty coordinate tuples (row, col).
        '''
        available_moves = []
        for r_idx, row in enumerate(self.grid):
            for c_idx, cell in enumerate(row):
                if cell == " ":
                    available_moves.append((r_idx, c_idx))
        return available_moves


# Driver execution
if __name__ == "__main__":
    gridd = GRID()
    gridd.build_grid()
    grid = gridd.get_grid()

    player2 = None
    case = True
    while case:
        player2 = input("Player 2 enter your symbol: ").strip()
        if player2.isalpha() and player2 != "AI":
            case = False

    game = MINIMAX(grid, player2)
    game.game()