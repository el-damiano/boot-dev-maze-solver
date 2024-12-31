import unittest
from maze import Maze


class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)

    def test_maze_create_zero_cells(self):
        num_rows = 0
        num_cols = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_rows)

        num_rows = 10
        num_cols = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)

    def test_maze_create_negative_amount_of_cells(self):
        num_rows = -10
        num_cols = -12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), 0)

    def test_maze_entrance_and_exit_walls_are_broken(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        maze_entrance = m1._cells[0][0]
        maze_exit = m1._cells[m1._num_rows - 1 ][m1._num_cols - 1]
        maze_entrance.has_left_wall == False
        maze_exit.has_bottom_wall == False
        self.assertFalse(maze_entrance.has_left_wall)
        self.assertFalse(maze_exit.has_bottom_wall)

    def test_maze_reset_cell_visits(self):
        num_cols = 10
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for row in m1._cells:
            for col in row:
                self.assertEqual(col.visited, False)


if __name__ == "__main__":
    unittest.main()
