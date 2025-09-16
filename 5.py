from window import Window
from structs.vector2 import Vector2
from ui.base_label import BaseLabel
from ui.base_entry import BaseEntry
from ui.base_button import BaseButton
from tkinter import messagebox

colors = ['white', 'green', 'red']

def main():
    window = Window()

    button = BaseButton(width=200, text='НАЖМЕЕ')
    entry = BaseEntry(Vector2(200, 200), width=200)

    button.onClickEvents.subscribe(lambda:messagebox.showinfo("Пук пук", entry.value.get()))

    window.loop()


if __name__ == "__main__":
    main()