from window import Window
from structs.vector2 import Vector2
from structs.report import Report
from ui.base_label import BaseLabel
from ui.base_entry import BaseEntry
from ui.base_button import BaseButton
from ui.base_combobox import BaseCombobox
from tkinter import messagebox, Widget
from repository import Repository

class Core:
    def __init__(self):
        self.service = ''
        self.price = 0
        self.window = Window[Widget]()
        self.repository = Repository()

        self.values = self.repository.get_services()
        

    def main(self):

        BaseLabel("АВТОСЕРВИС CAT & GO", Vector2(180, 50), "Arial 20")

        BaseLabel("Марка автомобиля", Vector2(50, 150))
        BaseLabel("Модель автомобиля", Vector2(50, 200))
        BaseLabel("Цвет:", Vector2(50, 250))
        BaseLabel("Год производства:", Vector2(50, 300))
        BaseLabel("Номер автомобиля:", Vector2(50, 350))

        BaseLabel("Фамилия:", Vector2(50, 450))
        BaseLabel("Имя:", Vector2(50, 500))
        BaseLabel("Номер телефона:", Vector2(50, 550))


        self.window.add_widget(BaseEntry(Vector2(270, 150),  150), 'entry_marka')
        self.window.add_widget(BaseEntry(Vector2(270, 200),  150), 'entry_model')
        self.window.add_widget(BaseEntry(Vector2(270, 250),  150), 'entry_color')
        self.window.add_widget(BaseEntry(Vector2(270, 300),  150), 'entry_year_build')
        self.window.add_widget(BaseEntry(Vector2(270, 350),  150), 'entry_number')


        self.window.add_widget(BaseEntry(Vector2(270, 450),  150), 'entry_surname')
        self.window.add_widget(BaseEntry(Vector2(270, 500),  150), 'entry_name')
        self.window.add_widget(BaseEntry(Vector2(270, 550),  150), 'entry_phone_number')

        write_btn = BaseButton("Записать", Vector2(500, 600), 100)
        write_btn.onClick.subscribe(lambda: self.print_file(self.window))
        

        self.services_box = BaseCombobox(Vector2(450, 200), self.values, 200, "Arial 13")
        BaseLabel("Наименование услуги:", Vector2(450, 150))

        self.services_box.onSelect.subscribe(lambda: self.show_price())

        self.window.loop()

    def show_price(self):
        self.service = self.services_box.combobox.get()
        self.price = self.values[self.service] if self.values[self.service] else 0
        new_label = BaseLabel("Цена: "+str(self.price)+ " руб.", Vector2(450, 250))

    def check_empty(self):
        if (
            self.window.get_widget('entry_marka', BaseEntry).get_value() == ""
            or self.window.get_widget('entry_model', BaseEntry).get_value() == ""
            or self.window.get_widget('entry_color', BaseEntry).get_value() == ""
            or self.window.get_widget('entry_year_build', BaseEntry).get_value() == ""
            or self.window.get_widget('entry_number', BaseEntry).get_value() == ""
            or self.service == ""
            or self.window.get_widget('entry_surname', BaseEntry).get_value() == ""
            or self.window.get_widget('entry_name', BaseEntry).get_value() == ""
            or self.window.get_widget('entry_phone_number', BaseEntry).get_value() == ""
        ):
            return False
        return True

    def print_file(self, window: Window):
        if not self.check_empty():
            messagebox.showerror("Ошибка", "Заполните все поля")
            return
        
        messagebox.showinfo("Сообщение", "Файл успешно создан")

        report = Report(window.get_widget('entry_marka', BaseEntry).get_value(),
                        window.get_widget('entry_model', BaseEntry).get_value(),
                        window.get_widget('entry_color', BaseEntry).get_value(),
                        window.get_widget('entry_year_build', BaseEntry).get_value(),
                        window.get_widget('entry_number', BaseEntry).get_value(),
                        window.get_widget('entry_surname', BaseEntry).get_value(),
                        window.get_widget('entry_name', BaseEntry).get_value(),
                        window.get_widget('entry_phone_number', BaseEntry).get_value(),
                        self.service,
                        self.price
                        )
        
        self.repository.create_report(report)

        file = open('new_otchet.txt', 'a', encoding='utf8')

        file.write("----------НОВЫЙ ЗАКАЗ----------\n")
        file.write("Фамилия, имя: " + report.surname + " " + report.name + "\n")
        file.write("Данные машины: " + report.model + " " + report.marka + "\n")
        file.write("Услсуга: " + report.service + " Стоимость: " + str(report.price) + " руб." + "\n")
        file.write("--------------------------------" + "\n")

        file.close()


if __name__ == "__main__":
    Core().main()