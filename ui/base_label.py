from structs.vector2 import Vector2
from tkinter import Label

class BaseLabel:
    def __init__(self, text: str = "", position: Vector2 = Vector2.zero(), font: str = "Arial 15", color: str = "lightblue"):
        self.text = text
        self.position = position
        self.font = font
        self.color = color

        self.label = Label(text=self.text, font=self.font, bg=self.color)
        self.label.place(x = self.position.x, y = self.position.y)