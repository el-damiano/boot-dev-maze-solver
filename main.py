from tkinter import Tk, BOTH, Canvas


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


def main():
    win = Window(800, 600)
    win.wait_for_close()


if __name__ == "__main__":
    main()
