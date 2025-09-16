from window import Window
from structs.vector2 import Vector2

colors = ['white', 'green', 'red']

def main():
    window = Window()
    
    pointer = 0

    for i in range(0, 10):
        if pointer == 3:
            pointer = 0

        color = colors[pointer]

        window.create_reactangle(Vector2(150 + i * 10, 150 + i * 10), Vector2(350 - i * 10, 350 - i * 10), fill=color, width=1, outline='black')
        pointer += 1

    window.loop()


if __name__ == "__main__":
    main()