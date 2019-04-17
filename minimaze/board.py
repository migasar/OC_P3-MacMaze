"""Gere le plateau de jeu et les interactions des objets"""


import settings as constants

from position import Position
from case import Case
 

class Board:

    def __init__(self, grid):

        self.grid = grid

    @classmethod
    def load_blueprint(cls, filename):

        grid = []

        with open(filename, 'r') as infile:
            content = [line.strip() for line in infile.readlines() if line.strip()]
            for y, line in enumerate(content):
                for x, col in enumerate(line):
                    if col == "S":
                        grid.append(Case(x+1, y+1, walk=True, landing="start", visual = col))
                    elif col == "G":
                        grid.append(Case(x+1, y+1, walk=True, landing="goal", visual = col))
                    elif col == ".":
                        grid.append(Case(x+1, y+1, walk=True, visual = col))
                    else:
                        grid.append(Case(x+1, y+1, walk=False, visual = col))

        return cls(grid)





"""
# TEST
def main():
    board = Board.load_blueprint(constants.blueprint)
    print(board.grid[0])


if __name__ == "__main__":
    main()
"""
