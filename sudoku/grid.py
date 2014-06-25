from __future__ import print_function

class Grid:

    def __init__(self):
        self.grid = [None] * 81

    def load_data(self, data_string, separator=","):
        """Take string with values split by given separator."""
        self.grid = [(lambda x: int(x) if x != '' else 0)(x) for x in data_string.split(separator)]

    def print_grid(self):
        print("+---+---+---+---+---+---+---+---+---+")
        for row in range(1,10):
            self.print_row(self.get_row(row))

    def print_row(self, row):
        for index, elm in enumerate(row):
            print("| ", end="")
            print(elm, end="")
            print(" ", end="")
            if index == len(row)-1:
                print("|")
        print("+---+---+---+---+---+---+---+---+---+")

    def get_grid(self):
        return self.grid

    def get_row(self, row_index):
        """Return requested row (top down from 1)"""
        # Because list indexing starts from 0
        row_index = row_index-1
        return self.grid[row_index*9:row_index*9+9]

    def get_column(self, column_index):
        """Return requested column (left to right from 1)"""
        # Because list indexing starts from 0
        column_index = column_index-1
        return self.grid[column_index::9]

    def get_square(self, square_index):
        """Return requested sub square (from top left by row)"""
        # Initial square position (top left) using tn = dn+(a-d)
        # with one extra because list index from 0
        initial = (((3*square_index)-2)-1)

        square = []

        square.extend(self.grid[initial:initial+3])
        square.extend(self.grid[initial+9:initial+12])
        square.extend(self.grid[initial+18:initial+21])
        return square
