from gui import Window, Line, Point
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(10, 10, 15, 15, 25, 25, win)
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
