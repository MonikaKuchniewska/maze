from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Generator")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas_game = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas_game.pack(fill=BOTH, expand=1)
        self.window_is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.window_is_running = True
        while self.window_is_running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas_game, fill_color)
    
    def close(self):
        self.window_is_running = False

    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1 
        self.point2 = point2 

    def draw(self, canvas, fill_color="black"):

        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)




