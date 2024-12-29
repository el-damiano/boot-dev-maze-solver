from tkinter import Tk, BOTH, Canvas


class Point():

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line():

    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)


class Window():

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("floating Maze Solver")  # include 'floating' so my WM won't tile it
        self.canvas = Canvas(width=self.width, height=self.height)
        self.canvas.pack()
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self) -> None:
        self.is_running = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.canvas, fill_color)


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
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

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



def main():
    win = Window(800, 600)

    # 3 stripes
    win.draw_line(Line(Point(0, 0), Point(800, 600)), "black")
    win.draw_line(Line(Point(00, 10), Point(800, 610)), "black")
    win.draw_line(Line(Point(00, -10), Point(800, 590)), "black")

    # red squares in the middle
    Cell(win, 350, 450, 250, 350, True, True, True, True).draw()
    Cell(win, 340, 460, 240, 360, False, True, True, True).draw()
    Cell(win, 330, 470, 230, 370, True, False, True, True).draw()
    Cell(win, 320, 480, 220, 380, True, True, False, True).draw()
    Cell(win, 310, 490, 210, 390, True, True, True, False).draw()

    Cell(win, 300, 500, 200, 400, False, False, True, True).draw()
    Cell(win, 290, 510, 190, 410, True, False, False, True).draw()
    Cell(win, 280, 520, 180, 420, True, True, False, False).draw()
    Cell(win, 270, 530, 170, 430, True, True, True, False).draw()
    Cell(win, 260, 540, 160, 440, False, True, True, True).draw()

    win.wait_for_close()


if __name__ == "__main__":
    main()
