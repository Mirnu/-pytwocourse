from structs.vector2 import Vector2
from tkinter import Entry, StringVar

class BaseEntry:
    def __init__(self, position: Vector2 = Vector2.zero(), width: int = 1, font: str = "Arial 15"):
        self.position = position
        self.font = font
        self.width = width

        self.value = StringVar()

        self.entry = Entry(font=self.font, textvariable=self.value)
        self.entry.place(x = self.position.x, y = self.position.y, width=self.width)

    def get_value(self):
        return self.value.get()