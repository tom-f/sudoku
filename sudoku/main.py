from grid import Grid
from textui import TextUi

class Main:

	def run(self):
		"""Main access point for application"""
        grid = Grid()
        puzzle_string = ",6,,2,9,4,,7,,2,,8,,,,9,,4,,9,,,5,,,2,,7,,,5,,3,,,2,9,,1,,,,5,,7,5,,,1,,9,,,3,,1,,,4,,,3,,3,,2,,,,7,,9,,4,,9,3,2,,1,"
        grid.load_data(puzzle_string)
        
        textUi = TextUi()
        textUi.print_grid(grid)
