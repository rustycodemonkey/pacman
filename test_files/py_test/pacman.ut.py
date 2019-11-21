"""
Unit tests for pacman.py
Last Modified: November 21, 2019
"""

# import os
# import sys
# import time
import unittest
from pacman import pacman


class AllTests(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(pacman("generic.txt"), (6, 1, 27))

    def test_no_walls(self):
        self.assertEqual(pacman("no_walls.txt"), (2, 1, 11))

    def test_no_walls_loop(self):
        self.assertEqual(pacman("no_walls_loop.txt"), (1, 1, 11))

    def test_no_walls_loops(self):
        self.assertEqual(pacman("no_walls_loops.txt"), (4, 1, 10))

    def test_trapped_middle(self):
        self.assertEqual(pacman("trapped_middle.txt"), (3, 3, 0))

    def test_trapped_corner(self):
        self.assertEqual(pacman("trapped_corner.txt"), (4, 4, 0))

    def test_edge(self):
        self.assertEqual(pacman("edge.txt"), (-1, -1, 0))

    def test_edge_perimeter(self):
        self.assertEqual(pacman("edge_perimeter.txt"), (-1, -1, 0))

    def test_edge_wall(self):
        self.assertEqual(pacman("edge_wall.txt"), (-1, -1, 0))

    def test_runtime(self):
        self.assertEqual(pacman("runtime.txt"), (2142, 147, 148))


if __name__ == '__main__':
    for testClass in [AllTests]:
        print('\n\nTest Class: {}\n'.format(testClass.__name__))
        suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
        result = unittest.TextTestRunner(verbosity=0).run(suite)
