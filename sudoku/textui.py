from __future__ import print_function
from grid import Grid

class TextUi:

    def print_grid(self, grid):
        print("+---+---+---+---+---+---+---+---+---+")
        for row in range(1,10):
            self.print_row(grid.get_row(row))

    def print_row(self, row):
        for index, elm in enumerate(row):
            print("| ", end="")
            print(elm, end="")
            print(" ", end="")
            if index == len(row)-1:
                print("|")
        print("+---+---+---+---+---+---+---+---+---+")
