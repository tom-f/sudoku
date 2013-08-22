import unittest
from sudoku.grid import Grid

class TestGrid(unittest.TestCase):

	def test_set_grid(self):
		"""Test loading data into a grid."""
		test_grid = self.load_grid_181()
		result_grid = test_grid.get_grid()

		self.assertEquals(result_grid, range(1, 82))

	def test_get_row_by_index(self):
		"""Test correct row is returned for given index"""	
		test_grid = self.load_grid_181()
		result_row = test_grid.row(4)

		self.assertEquals(result_row, range(28, 37))

	def load_grid_181(self):
		""""Helper function to load a grid filled with values 1 to 81"""
		test_grid = Grid()
		expected_string = ','.join((str(x) for x in range(1,82)))
		test_grid.load_data(expected_string)

		return test_grid