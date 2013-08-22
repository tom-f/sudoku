from grid import Grid

class Main:

	def run(self):
		"""Main access point for application"""
		grid = Grid()
		expected_string = ','.join((str(x) for x in range(1,82)))
		grid.load_data(expected_string)
		grid.print_grid()

		print "\n"
		print "\n"

		col = grid.get_column(2)
		print col
