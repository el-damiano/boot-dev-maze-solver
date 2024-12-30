import time

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
            win = None) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = list()

        self._create_cells()

    def _create_cells(self) -> None:

        for row in range(0, self._num_rows):
            self._cells.append(list())
            for col in range(0, self._num_cols):
                self._cells[row].append(Cell(self._win))

        for row in range(0, self._num_rows):
            for col in range(0, self._num_cols):
                self._draw_cell(row, col)

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
