import unittest
from sudoku.grid import Grid

class TestGrid(unittest.TestCase):

	def test_set_grid(self):
		"""Test loading data into a grid."""
		test_grid = Grid()

		expected_list = range(1,82)
		expected_string = ','.join((str(x) for x in expected_list))

		test_grid.load_data(expected_string)
		result_grid = test_grid.get_grid()

		self.assertEquals(result_grid, expected_list)
