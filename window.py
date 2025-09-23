from tkinter import Canvas, Tk, Widget
from structs.vector2 import Vector2
from typing import TypeVar, Dict, Generic, Optional, cast

T = TypeVar('T', bound=Widget)

class Window(Generic[T]): 
    def __init__(self, size: Vector2= Vector2(670, 670), geometry="700x700"):
        self.window = Tk()

        self.widgets: Dict[str, T] = {}

        self.window.geometry(geometry)

        self.window.title("window")

        self.window.configure(bg="blue")

        self.window.resizable(False, False)

        self.__my_canva(size)

    def __my_canva(self, size: Vector2):
        self.canva = Canvas(width=size.x, height=size.y, bg="lightblue")
        self.canva.pack()

    def create_line(self, vector1: Vector2, vector2: Vector2, fill: str = 'red', width: int = 5):
        self.canva.create_line(vector1.to_tuple(), vector2.to_tuple(), fill=fill, width=width)

    def create_reactangle(self, vector1: Vector2, vector2: Vector2, fill: str = 'yellow', outline: str = 'red', width: int = 5):
        self.canva.create_rectangle(vector1.to_tuple(), vector2.to_tuple(), fill=fill, width=width, outline=outline)

    def create_oval(self, vector1: Vector2, vector2: Vector2, fill: str = 'yellow', outline: str = 'red', width: int = 5):
        self.canva.create_oval(vector1.to_tuple(), vector2.to_tuple(), fill=fill, width=width, outline=outline)

    def add_widget(self, widget: Widget, key: str):
        self.widgets[key] = widget
        return widget

    def get_widget(self, key: str, cls: type[T] = Widget) -> Optional[T]:
        widget = self.widgets.get(key)
        if isinstance(widget, cls):
            return widget
        return None

    def loop(self): 
        self.window.mainloop()