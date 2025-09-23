from window import Window
from structs.vector2 import Vector2
from ui.base_label import BaseLabel
from ui.base_entry import BaseEntry
from ui.base_button import BaseButton
from ui.base_combobox import BaseCombobox
from tkinter import messagebox, Widget
import psycopg2


class Core:
    def __init__(self):
        self.service = ''
        self.price = 0
        self.window = Window[Widget]()

        self.values = {}

        connector = psycopg2.connect(
            host="localhost",
            database="sharaga",
            user="postgres",
            password="postgres",
        )

        cursor = connector.cursor()

        cursor.execute("SELECT * FROM services")
        rows = cursor.fetchall()

        for row in rows:
            self.values[row[1]] = row[2]

        connector.commit()

        cursor.close()
        connector.close()
        

    def main(self):

        label_title = BaseLabel("АВТОСЕРВИС CAT & GO", Vector2(180, 50), "Arial 20")

        label_marka = BaseLabel("Марка автомобиля", Vector2(50, 150))
        label_model = BaseLabel("Модель автомобиля", Vector2(50, 200))
        label_color = BaseLabel("Цвет:", Vector2(50, 250))
        year_build = BaseLabel("Год производства:", Vector2(50, 300))
        car_number = BaseLabel("Номер автомобиля:", Vector2(50, 350))

        entry_marka = self.window.add_widget(BaseEntry(Vector2(270, 150),  150), 'entry_marka')
        entry_model = self.window.add_widget(BaseEntry(Vector2(270, 200),  150), 'entry_model')
        entry_color = self.window.add_widget(BaseEntry(Vector2(270, 250),  150), 'entry_color')
        entry_year_build = self.window.add_widget(BaseEntry(Vector2(270, 300),  150), 'entry_year_build')
        entry_number = self.window.add_widget(BaseEntry(Vector2(270, 350),  150), 'entry_number')

        write_btn = BaseButton("Записать", Vector2(500, 600), 100)
        write_btn.onClick.subscribe(lambda: self.print_file(self.window))
        

        self.services_box = BaseCombobox(Vector2(450, 200), self.values, 200, "Arial 13")
        car_service = BaseLabel("Наименование услуги:", Vector2(450, 150))

        self.services_box.onSelect.subscribe(lambda: self.show_price())

        self.window.loop()

    def show_price(self):
        self.service = self.services_box.combobox.get()
        self.price = self.values[self.service] if self.values[self.service] else 0
        new_label = BaseLabel("Цена: "+str(self.price)+ " руб.", Vector2(450, 250))

    def print_file(self, window: Window):
        file = open('new_otchet.txt', 'w', encoding='utf8')

        file.write("Марка автомобиля:"+window.get_widget('entry_marka', BaseEntry).get_value()+"\n")
        file.write("Модель автомобиля:"+window.get_widget('entry_marka', BaseEntry).get_value()+"\n")
        file.write("Цвет:"+window.get_widget('entry_marka', BaseEntry).get_value()+"\n")
        file.write("Год производства:"+window.get_widget('entry_marka', BaseEntry).get_value()+"\n")
        file.write("Номер автомобиля:"+window.get_widget('entry_marka', BaseEntry).get_value()+"\n")

        file.write("Услуга: " + self.service + "\n")
        file.write("Стоимость: " + str(self.price) + "\n")

        file.close()


if __name__ == "__main__":
    Core().main()