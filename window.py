from tkinter import Canvas, Tk, Widget
from structs.vector2 import Vector2

class Window: 
    def __init__(self):
        self.window = Tk()

        self.widgets = dict()

        self.window.geometry("500x600")

        self.window.title("window")

        self.window.configure(bg="lightblue")

        self.window.resizable(False, False)

        self.__my_canva()

    def __my_canva(self):
        self.canva = Canvas(width=470, height=570, bg="blue")
        self.canva.pack()

    def create_line(self, vector1: Vector2, vector2: Vector2, fill: str = 'red', width: int = 5):
        self.canva.create_line(vector1.to_tuple(), vector2.to_tuple(), fill=fill, width=width)

    def create_reactangle(self, vector1: Vector2, vector2: Vector2, fill: str = 'yellow', outline: str = 'red', width: int = 5):
        self.canva.create_rectangle(vector1.to_tuple(), vector2.to_tuple(), fill=fill, width=width, outline=outline)

    def create_oval(self, vector1: Vector2, vector2: Vector2, fill: str = 'yellow', outline: str = 'red', width: int = 5):
        self.canva.create_oval(vector1.to_tuple(), vector2.to_tuple(), fill=fill, width=width, outline=outline)

    def register_widget(self, widget: Widget, key: str):
        self.widgets[key] = widget

    def get_widget(self, key: str) -> Widget:
        return self.widgets[key]

    def loop(self): 
        self.window.mainloop()