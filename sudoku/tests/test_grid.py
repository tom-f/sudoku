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
		result_row = test_grid.get_row(4)

		self.assertEquals(result_row, range(28, 37))

	def test_get_column_by_index(self):
		"""Test correct column is returned for given index"""
		test_grid = self.load_grid_181()
		result_column = test_grid.get_column(2)

		self.assertEquals(result_column, range(2,82,9))

	def test_get_square_by_index(self):
		"""Test correct sub-square is returned for given index"""
		test_grid = self.load_grid_181()
		result_square = test_grid.get_square(1)

		expected_square = [1, 2, 3, 10, 11, 12, 19, 20, 21]

		self.assertEqual(result_square, expected_square)

	def load_grid_181(self):
		""""Helper function to load a grid filled with values 1 to 81"""
		test_grid = Grid()
		expected_string = ','.join((str(x) for x in range(1,82)))
		test_grid.load_data(expected_string)

		return test_grid