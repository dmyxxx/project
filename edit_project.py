from PyQt6 import QtWidgets
import sys
import database

class EditProject(QtWidgets.QWidget):
    def __init__(self, db, main_app, project_id):
        super(EditProject, self).__init__()
        self.db = db
        self.main_app = main_app
        self.project_id = project_id
        self.init_ui()

    # def init_ui(self):
    #     self.project = self.db.get_project(self.project_id)
    #
    #     if self.project is not None:
    #         self.name_label = QtWidgets.QLabel('Название проекта:')
    #         self.name_input = QtWidgets.QLineEdit(self.project[1])
    #         self.description_label = QtWidgets.QLabel('Описание проекта:')
    #         self.description_input = QtWidgets.QTextEdit(self.project[2])
    #         self.manager_label = QtWidgets.QLabel('ID менеджера:')
    #         self.manager_input = QtWidgets.QLineEdit(str(self.project[3]))
    #         self.start_date_label = QtWidgets.QLabel('Дата начала:')
    #         self.start_date_input = QtWidgets.QLineEdit(self.project[4])
    #         self.end_date_label = QtWidgets.QLabel('Дата окончания:')
    #         self.end_date_input = QtWidgets.QLineEdit(self.project[5])
    #         self.update_button = QtWidgets.QPushButton('Обновить проект')
    #
    #         layout = QtWidgets.QVBoxLayout()
    #         layout.addWidget(self.name_label)
    #         layout.addWidget(self.name_input)
    #         layout.addWidget(self.description_label)
    #         layout.addWidget(self.description_input)
    #         layout.addWidget(self.manager_label)
    #         layout.addWidget(self.manager_input)
    #         layout.addWidget(self.start_date_label)
    #         layout.addWidget(self.start_date_input)
    #         layout.addWidget(self.end_date_label)
    #         layout.addWidget(self.end_date_input)
    #         layout.addWidget(self.update_button)
    #
    #         self.setLayout(layout)
    #
    #         self.apply_button = QtWidgets.QPushButton('Применить')
    #         self.back_button = QtWidgets.QPushButton('Назад')
    #
    #         layout.addWidget(self.apply_button)
    #         layout.addWidget(self.back_button)
    #
    #         self.setLayout(layout)
    #
    #         self.apply_button.clicked.connect(self.update_project)
    #         self.back_button.clicked.connect(self.main_app.switch_to_main_menu)
    #
    #         self.update_button.clicked.connect(self.update_project)
    #     else:
    #         print(f"Проект с ID {self.project_id} не найден в базе данных.")

    def init_ui(self):
        self.project = self.db.get_project(self.project_id)

        if self.project is not None:
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
            print(f"Проект с ID {self.project_id} не найден в базе данных.")


    def update_project(self):
        name = self.name_input.text()
        description = self.description_input.toPlainText()
        manager_id = int(self.manager_input.text())
        start_date = self.start_date_input.text()
        end_date = self.end_date_input.text()
        self.db.update_project(self.project_id, name, description, manager_id, start_date, end_date)
        print('Проект успешно обновлен')


def main():
    app = QtWidgets.QApplication(sys.argv)
    # Замените следующую строку на фактический project_id, который вы хотите отредактировать
    project_id = 1
    edit_project = EditProject(project_id)
    edit_project.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()