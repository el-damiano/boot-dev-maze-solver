from gui import Window, Line, Point


class Cell():

    def __init__(self,
                 win: Window,
                 x1: int,
                 x2: int,
                 y1: int,
                 y2: int,
                 has_left_wall = True,
                 has_right_wall = True,
                 has_top_wall = True,
                 has_bottom_wall = True) -> None:
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self) -> None:
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        if self.has_left_wall:
            line = Line(top_left, bottom_left)
            self._win.draw_line(line, "red")
        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            self._win.draw_line(line, "red")
        if self.has_top_wall:
            line = Line(top_left, top_right)
            self._win.draw_line(line, "red")
        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self._win.draw_line(line, "red")
