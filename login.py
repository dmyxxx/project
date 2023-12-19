import sys

from PyQt6 import QtWidgets
import database
from registration import RegistrationDialog  # Импортируйте новый класс

class LoginScreen(QtWidgets.QWidget):


    def __init__(self, db):
        super(LoginScreen, self).__init__(None)
        self.db = db
        self.init_ui()

    def init_ui(self):
        self.username_label = QtWidgets.QLabel('Логин:')
        self.username_input = QtWidgets.QLineEdit()
        self.password_label = QtWidgets.QLabel('Пароль:')
        self.password_input = QtWidgets.QLineEdit()
        self.login_button = QtWidgets.QPushButton('Войти')
        self.register_button = QtWidgets.QPushButton('Регистрация')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.show_registration_dialog)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        user = self.db.get_user(username)
        if user and user[2] == password:
            if username == 'admin' and password == 'admin':
                print('Вход администратора успешен')
            else:
                print('Вход успешен')
        else:
            print('Вход не удался')
            self.show_registration_dialog()  # Показать диалоговое окно регистрации

    def show_registration_dialog(self):
        registration_dialog = RegistrationDialog(self)
        registration_dialog.exec()

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        self.db.add_user(username, password, 'user')
        print('Регистрация успешна')

    def show_registration_dialog(self):
        registration_dialog = RegistrationDialog(self)
        registration_dialog.exec()
