import math
import time
import random

from cell import Cell


class Maze():

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = list()

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self) -> None:

        for row in range(0, self._num_rows):
            self._cells.append(list())
            for col in range(0, self._num_cols):
                self._cells[row].append(Cell(self._win))

        for row in range(0, self._num_rows):
            for col in range(0, self._num_cols):
                self._draw_cell(row, col)

    def _break_entrance_and_exit(self) -> None:
        if not len(self._cells) or not len(self._cells[0]):
            return

        maze_entrance = self._cells[0][0]
        maze_entrance.has_left_wall = False
        self._draw_cell(0, 0)

        maze_exit = self._cells[self._num_rows - 1 ][self._num_cols - 1]
        maze_exit.has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

        self._break_walls_r(0,0)

    def _break_walls_r(self, row_curr, col_curr) -> None:
        current_cell: Cell = self._cells[row_curr][col_curr]
        current_cell.visited = True

        reached_the_end = current_cell == self._cells[self._num_rows - 1 ][self._num_cols - 1]
        if reached_the_end:
            return

        while True:
            to_visit = []
            vector_by_direction = {
                'up': [-1, 0],
                'right': [0, 1],
                'down': [1, 0],
                'left': [0, -1],
            }

            for dir, vector in vector_by_direction.items():
                r, c = vector
                if r < 0 or c < 0:
                    continue

                row_adjacent = row_curr + r
                col_adjacent = col_curr + c

                if row_adjacent == self._num_rows or col_adjacent == self._num_rows:
                    continue

                if self._cells[row_adjacent][col_adjacent]:
                    to_visit.append(dir)

            if len(to_visit) == 0:
                return

            random_dir = random.choice(to_visit)
            row_to_visit, col_to_visit = vector_by_direction[random_dir]
            row_to_visit += row_curr
            col_to_visit += col_curr

            next_cell = self._cells[row_to_visit][col_to_visit]

            match random_dir:
                case 'up':
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                case 'right':
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False
                    pass
                case 'down':
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                    pass
                case 'left':
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False
                    pass
                case _:
                    return

            self._draw_cell(row_curr, col_curr)
            self._break_walls_r(row_to_visit, col_to_visit)
            break

    def _draw_cell(self, row, col) -> None:
        if self._win is None:
            return

        cell_x1 = self._x1 + (self._cell_size_x * col)
        cell_y1 = self._y1 + (self._cell_size_y * row)
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y

        self._cells[row][col].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.02)
