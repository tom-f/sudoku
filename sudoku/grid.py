
class Grid:

	def __init__(self):
		self.grid = [None] * 81

	def load_data(self, data_string, separator=","):
		"""Take string with values split by given seperator."""
		self.grid = [int(x) for x in data_string.split(separator)]

	def print_grid(self):
		for row in range(9):
			row = self.grid[9*row:9*row+9]
			print row

	def get_grid(self):
		return self.grid

	def row(self, index):
		row = index/9
		return self.grid[row*9:row*9*9]

	def coloumn(self, index):
		pass

	def square(self, index):
		pass
