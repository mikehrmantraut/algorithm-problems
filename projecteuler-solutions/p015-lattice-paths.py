# Project Euler Problem 15
# Lattice Paths
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
import eulerlib
# This is a classic combinatorics problem. To get from the top left corner to the bottom right corner of an N*N grid,
# it involves making exactly N moves right and N moves down in some order. Because each individual down or right move
# is indistinguishable, there are exactly 2N choose N (binomial coefficient) ways of arranging these moves.
def compute():
	return str(eulerlib.binomial(40, 20))

if __name__ == "__main__":
	print(compute())
