import unittest
from maze_generator import Maze
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols,)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows,)

    def test_maze_minimal_dimensions(self):
        m1 = Maze(0, 0, 1, 1, 10, 10)
        self.assertEqual(len(m1._Maze__cells), 1)
        self.assertEqual(len(m1._Maze__cells[0]), 1)

    def test_cells_are_instances_of_cell(self):
        m1 = Maze(0, 0, 5, 5, 10, 10)
        for col in m1._Maze__cells:
            for cell in col:
                self.assertIsInstance(cell, Cell)

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols,)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows,)


    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._Maze__cells[0][0].has_top_wall, False,)
        self.assertEqual(m1._Maze__cells[num_cols - 1][num_rows - 1]. has_bottom_wall, False,)

    def test_maze_reset_cells_visited(self):
        m1 = Maze(0, 0, 3, 3, 10, 10)

        for col in m1._Maze__cells:
            for cell in col:
                cell.visited = True

        m1._Maze__reset_cells_visited()

        for col in m1._Maze__cells:
            for cell in col:
                self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()