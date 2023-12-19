from PyQt6 import QtWidgets
from project_selection import ProjectSelection  # Импортируйте новый класс

class MainMenu(QtWidgets.QWidget):
    def __init__(self, db, main_app):
        super(MainMenu, self).__init__()
        self.db = db
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        self.new_project_button = QtWidgets.QPushButton('Создать новый проект')
        self.view_projects_button = QtWidgets.QPushButton('Просмотреть проекты')
        self.edit_project_button = QtWidgets.QPushButton('Редактировать проект')
        self.delete_project_button = QtWidgets.QPushButton('Удалить проект')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.new_project_button)
        layout.addWidget(self.view_projects_button)
        layout.addWidget(self.edit_project_button)
        layout.addWidget(self.delete_project_button)

        self.setLayout(layout)

        self.new_project_button.clicked.connect(self.main_app.switch_to_create_project)
        self.view_projects_button.clicked.connect(self.main_app.switch_to_view_projects)
        self.edit_project_button.clicked.connect(self.switch_to_project_selection)
        self.delete_project_button.clicked.connect(self.main_app.switch_to_delete_project)

    def switch_to_project_selection(self):
        self.hide()
        self.project_selection = ProjectSelection(self.db, self)
        self.project_selection.show()