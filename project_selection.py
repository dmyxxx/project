from PyQt6 import QtWidgets


class ProjectSelection(QtWidgets.QWidget):
    def __init__(self, db, main_app):
        super(ProjectSelection, self).__init__()
        self.db = db
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        self.projects_list = QtWidgets.QListWidget()
        self.edit_button = QtWidgets.QPushButton('Редактировать выбранный проект')

        self.edit_button.clicked.connect(self.edit_selected_project)

    def edit_selected_project(self):
        selected_project_id = self.get_selected_project_id()
        if selected_project_id is not None:
            self.main_app.switch_to_edit_project(selected_project_id)

    # def get_selected_project_id(self):
    #     # Вернуть ID выбранного проекта или None, если проект не выбран
    #     pass