from gui import Window, Line, Point


class Cell():

    def __init__(self,
                 win: Window,
                 x1: int,
                 x2: int,
                 y1: int,
                 y2: int,
                 has_top_wall = True,
                 has_right_wall = True,
                 has_bottom_wall = True,
                 has_left_wall = True) -> None:
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_left_wall = has_left_wall

    def draw(self) -> None:
        if self._win is None:
            return

        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        if self.has_top_wall:
            line = Line(top_left, top_right)
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self._win.draw_line(line)
        if self.has_left_wall:
            line = Line(top_left, bottom_left)
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo = False) -> None:
        fill_color = "red"
        if undo:
            fill_color = "gray"

        half_x1 = abs(self._x2 - self._x1) // 2
        half_y1 = abs(self._y2 - self._y1) // 2
        center_x1 = self._x1 + half_x1
        center_y1 = self._y1 + half_y1

        half_x2 = abs(to_cell._x2 - to_cell._x1) // 2
        half_y2 = abs(to_cell._y2 - to_cell._y1) // 2
        center_x2 = to_cell._x1 + half_x2
        center_y2 = to_cell._y1 + half_y2

        line = Line(Point(center_x1, center_y1), Point(center_x2, center_y2))
        self._win.draw_line(line, fill_color)
