from structs.vector2 import Vector2
from tkinter.ttk import Combobox
from utils.observer import Observer
from typing import Dict

class BaseCombobox:
    def __init__(self, position: Vector2 = Vector2.zero(), values: Dict[str, any] = {}, width: int = 1, font: str = "Arial 15"):
        self.position = position
        self.font = font
        self.width = width
        self.values = values
        self.onSelect = Observer()

        self.combobox = Combobox(values=list(self.values.keys()), font=self.font, state="readonly")
        self.combobox.place(x = self.position.x, y = self.position.y, width=self.width)
        self.combobox.bind('<<ComboboxSelected>>', lambda event: self.select())

    def select(self):
        self.onSelect.notify()