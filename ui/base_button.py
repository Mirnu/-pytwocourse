from structs.vector2 import Vector2
from tkinter import Button
from utils.observer import Observer

class BaseButton:
    def __init__(self, text: str = "", position: Vector2 = Vector2.zero(), font: str = "Arial 15", width: int = 1,):
        self.text = text
        self.position = position
        self.font = font
        self.width = width
        self.onClickEvents = Observer()

        self.button = Button(text=self.text, font=self.font, command=self.onClick)
        self.button.place(x = self.position.x, y = self.position.y, width=self.width)

    def onClick(self):
        self.onClickEvents.notify()