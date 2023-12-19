from PyQt6 import QtWidgets
import sys
import database

class CreateProject(QtWidgets.QWidget):

    def __init__(self, main_app, db):  # Добавьте main_app в качестве аргумента
        super(CreateProject, self).__init__()
        self.main_app = main_app  # Сохраните main_app как атрибут экземпляра
        self.db = db
        self.init_ui()

    def init_ui(self):
        self.name_label = QtWidgets.QLabel('Название проекта:')
        self.name_input = QtWidgets.QLineEdit()
        self.description_label = QtWidgets.QLabel('Описание проекта:')
        self.description_input = QtWidgets.QTextEdit()
        self.manager_label = QtWidgets.QLabel('ID менеджера:')
        self.manager_input = QtWidgets.QLineEdit()
        self.start_date_label = QtWidgets.QLabel('Дата начала:')
        self.start_date_input = QtWidgets.QLineEdit()
        self.end_date_label = QtWidgets.QLabel('Дата окончания:')
        self.end_date_input = QtWidgets.QLineEdit()
        self.create_button = QtWidgets.QPushButton('Создать проект')



        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_input)
        layout.addWidget(self.manager_label)
        layout.addWidget(self.manager_input)
        layout.addWidget(self.start_date_label)
        layout.addWidget(self.start_date_input)
        layout.addWidget(self.end_date_label)
        layout.addWidget(self.end_date_input)
        layout.addWidget(self.create_button)

        self.setLayout(layout)

        self.create_button.clicked.connect(self.create_project)

        self.back_button = QtWidgets.QPushButton('Назад')  # новая кнопка "Назад"
        layout.addWidget(self.back_button)
        self.back_button.clicked.connect(self.main_app.switch_to_main_menu)
        self.setLayout(layout)

    def create_project(self):
        try:
            name = self.name_input.text()
            description = self.description_input.toPlainText()
            manager_id = int(self.manager_input.text())
            start_date = self.start_date_input.text()
            end_date = self.end_date_input.text()

            # Проверка ввода
            if not name or not description or not manager_id or not start_date or not end_date:
                print('Все поля должны быть заполнены')
                return

            # Валидация дат
            if start_date > end_date:
                print('Дата окончания проекта не может быть раньше даты его начала')
                return

            # Проверка существования менеджера
            manager = self.db.get_user_by_id(manager_id)
            if not manager:
                print('Менеджер с таким ID не существует')
                return

            self.db.add_project(name, description, manager_id, start_date, end_date)
            print('Проект успешно создан')
            self.main_app.switch_to_main_menu()
        except Exception as e:
            print(f"Произошла ошибка: {e}")

