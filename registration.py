from PyQt6 import QtWidgets
import database  # Импортируйте модуль базы данных

class RegistrationDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(RegistrationDialog, self).__init__(parent)
        self.db = database.Database()  # Инициализируйте базу данных
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Регистрация')
        self.setGeometry(100, 100, 400, 200)

        self.name_label = QtWidgets.QLabel('Имя:')
        self.name_input = QtWidgets.QLineEdit()
        self.surname_label = QtWidgets.QLabel('Фамилия:')
        self.surname_input = QtWidgets.QLineEdit()
        self.username_label = QtWidgets.QLabel('Логин:')
        self.username_input = QtWidgets.QLineEdit()
        self.password_label = QtWidgets.QLabel('Пароль:')
        self.password_input = QtWidgets.QLineEdit()
        self.register_button = QtWidgets.QPushButton('Зарегистрироваться')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.surname_label)
        layout.addWidget(self.surname_input)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

        self.register_button.clicked.connect(self.register)

    def register(self):
        name = self.name_input.text()
        surname = self.surname_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        self.db.add_user(username, password, 'user')  # Добавить пользователя в базу данных
        print(f'Пользователь {name} {surname} успешно зарегистрирован')
        self.close()