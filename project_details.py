import sys

from PyQt6 import QtWidgets
import database

class ProjectDetails(QtWidgets.QWidget):
    def __init__(self, project_id):
        super(ProjectDetails, self).__init__()
        self.db = database.Database()
        self.project_id = project_id
        self.init_ui()

    def init_ui(self):
        self.project = self.db.get_project(self.project_id)

        if self.project:
            self.name_label = QtWidgets.QLabel('Название проекта:')
            self.name_value = QtWidgets.QLabel(self.project[1])
            self.description_label = QtWidgets.QLabel('Описание проекта:')
            self.description_value = QtWidgets.QLabel(self.project[2])
            self.manager_label = QtWidgets.QLabel('ID менеджера:')
            self.manager_value = QtWidgets.QLabel(str(self.project[3]))
            self.start_date_label = QtWidgets.QLabel('Дата начала:')
            self.start_date_value = QtWidgets.QLabel(self.project[4])
            self.end_date_label = QtWidgets.QLabel('Дата окончания:')
            self.end_date_value = QtWidgets.QLabel(self.project[5])

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(self.name_label)
            layout.addWidget(self.name_value)
            layout.addWidget(self.description_label)
            layout.addWidget(self.description_value)
            layout.addWidget(self.manager_label)
            layout.addWidget(self.manager_value)
            layout.addWidget(self.start_date_label)
            layout.addWidget(self.start_date_value)
            layout.addWidget(self.end_date_label)
            layout.addWidget(self.end_date_value)

            self.setLayout(layout)
        else:
            # Handle the case where the project is not found
            error_label = QtWidgets.QLabel('Проект не найден')
            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(error_label)
            self.setLayout(layout)

def main():
    app = QtWidgets.QApplication(sys.argv)
    project_id = 1  # Replace this with the actual project ID you want to display
    project_details = ProjectDetails(project_id)
    project_details.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()