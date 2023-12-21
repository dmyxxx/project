from PyQt6 import QtWidgets
import pandas as pd

class ServiceSelection(QtWidgets.QWidget):
    def __init__(self, main_app):
        super(ServiceSelection, self).__init__()
        self.main_app = main_app
        self.services = [
            'Установка окон - 100',
            'Укладка керамической плитки - 200',
            'Монтаж гипсокартонных стен - 100',
            'Установка сантехники - 200',
            'Электромонтажные работы - 300',
            'Укладка паркетного пола - 400',
            'Малярные работы - 500',
            'Установка кровли - 600',
            'Утепление стен - 700',
            'Строительство фундамента - 800',
            'Монтаж системы отопления - 900',
            'Установка дверей - 1000',
            'Установка потолков - 1100',
            'Строительство бассейнов - 1200',
        ]
        self.init_ui()

    def init_ui(self):
        self.services_list = QtWidgets.QListWidget()
        self.services_list.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.calculate_button = QtWidgets.QPushButton('Рассчитать')
        self.back_button = QtWidgets.QPushButton('Назад')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.services_list)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

        self.calculate_button.clicked.connect(self.calculate_total)
        self.back_button.clicked.connect(self.main_app.switch_to_main_menu)

        # Добавьте услуги в QListWidget
        for service in self.services:
            item = QtWidgets.QListWidgetItem(service)
            self.services_list.addItem(item)

    def calculate_total(self):
        try:
            total = 0
            services = []
            for item in self.services_list.selectedItems():
                # Предполагается, что цена указана после последнего дефиса
                service, price = item.text().rsplit('-', 1)
                service = service.strip()
                price = float(price.strip())
                total += price
                services.append({'Услуга': service, 'Цена': price})

            print(f'\nОбщая стоимость выбранных услуг: {total}')

            # Добавляем общую стоимость в список услуг
            services.append({'Услуга': 'Общая стоимость', 'Цена': total})

            # Сохранение данных в файл Excel
            df = pd.DataFrame(services)
            df.to_excel('services.xlsx', index=False)
            print('Данные успешно сохранены в файл Excel.')
        except Exception as e:
            print(f'Произошла ошибка: {e}')

        # Возвращаем пользователя на главный экран
        self.main_app.switch_to_main_menu()