from PyQt6 import QtWidgets
import sys
import database

class EditProject(QtWidgets.QWidget):
    def __init__(self, db, main_app, project_id):
        super(EditProject, self).__init__()
        self.db = db
        self.main_app = main_app
        self.project_id = project_id
        self.project = self.db.get_project(self.project_id)
        self.init_ui()

    def init_ui(self):
        if self.project:
            self.name_input = QtWidgets.QLineEdit(self.project[1])
            self.description_input = QtWidgets.QTextEdit(self.project[2])
            self.manager_input = QtWidgets.QLineEdit(str(self.project[3]))
            self.start_date_input = QtWidgets.QLineEdit(self.project[4])
            self.end_date_input = QtWidgets.QLineEdit(self.project[5])
            self.update_button = QtWidgets.QPushButton('Обновить проект')

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(self.name_input)
            layout.addWidget(self.description_input)
            layout.addWidget(self.manager_input)
            layout.addWidget(self.start_date_input)
            layout.addWidget(self.end_date_input)
            layout.addWidget(self.update_button)

            self.setLayout(layout)

            self.update_button.clicked.connect(self.update_project)
        else:
            self.error_label = QtWidgets.QLabel(f"Проект с ID {self.project_id} не найден")
            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(self.error_label)
            self.setLayout(layout)

    def update_project(self):
        name = self.name_input.text()
        description = self.description_input.toPlainText()
        manager_id = int(self.manager_input.text())
        start_date = self.start_date_input.text()
        end_date = self.end_date_input.text()
        self.db.update_project(self.project_id, name, description, manager_id, start_date, end_date)
        print('Проект успешно обновлен')
        self.main_app.switch_to_main_menu()