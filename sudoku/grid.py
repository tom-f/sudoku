
class Grid:

	def __init__(self):
		self.grid = [None] * 81

	def print_grid(self):
		for row in range(9):
			row = self.grid[9*row:9*row+9]
			print row

	def row(self, index):
		pass

	def coloumn(self, index):
		pass

	def square(self, index):
		pass