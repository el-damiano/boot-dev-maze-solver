from gui import Window, Line, Point
from cell import Cell


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
