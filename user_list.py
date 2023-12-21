from PyQt6 import QtWidgets

class UserList(QtWidgets.QWidget):
    def __init__(self, db, main_app):
        super(UserList, self).__init__()
        self.db = db
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        self.user_list = QtWidgets.QListWidget()
        self.back_button = QtWidgets.QPushButton('Назад')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.user_list)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

        self.back_button.clicked.connect(self.main_app.switch_to_main_menu)

        self.refresh_user_list()

    def refresh_user_list(self):
        self.user_list.clear()
        users = self.db.get_all_users()
        for user in users:
            item = QtWidgets.QListWidgetItem(user[1])  # Предполагается, что имя пользователя находится во втором столбце
            self.user_list.addItem(item)
