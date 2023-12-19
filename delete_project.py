from PyQt6 import QtWidgets
import sys
import database

class DeleteProject(QtWidgets.QWidget):
    def __init__(self, db, main_app):
        super(DeleteProject, self).__init__()
        self.db = db
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        self.project_id_label = QtWidgets.QLabel('ID проекта:')
        self.project_id_input = QtWidgets.QLineEdit()
        self.confirm_button = QtWidgets.QPushButton('Удалить проект')
        self.back_button = QtWidgets.QPushButton('Назад')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.project_id_label)
        layout.addWidget(self.project_id_input)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

        self.confirm_button.clicked.connect(self.delete_project)
        self.back_button.clicked.connect(self.main_app.switch_to_main_menu)

    def delete_project(self):
        project_id = int(self.project_id_input.text())
        self.db.delete_project(project_id)
        print('Проект успешно удален')