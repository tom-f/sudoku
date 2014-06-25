from grid import Grid

class Solver:

	def __init__(self):
		self.current_puzzle = []
		self.guess_point = []

	def solve(self, grid):
        for index, elm in enumerate(grid):
            potentials = self.get_potential_values(elm)
            if len(potentials) == 1:
                grid[index] = potentials[0]


    def get_potential_values(self, current_value):
        return range(1, 10)
