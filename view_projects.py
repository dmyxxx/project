import sys

from PyQt6 import QtWidgets
import database

class ViewProjects(QtWidgets.QWidget):
    def __init__(self, db, main_app):
        super(ViewProjects, self).__init__()
        self.db = db
        self.main_app = main_app
        self.init_ui()
    # def init_ui(self):
    #     self.projects_list = QtWidgets.QListWidget()
    #     self.refresh_button = QtWidgets.QPushButton('Обновить список проектов')
    #
    #     layout = QtWidgets.QVBoxLayout()
    #     layout.addWidget(self.projects_list)
    #     layout.addWidget(self.refresh_button)
    #
    #     self.setLayout(layout)
    #
    #     self.refresh_button.clicked.connect(self.refresh_projects_list)

    def init_ui(self):
        self.projects_list = QtWidgets.QListWidget()
        self.refresh_button = QtWidgets.QPushButton('Обновить список проектов')
        self.back_button = QtWidgets.QPushButton('Назад')

        layout = QtWidgets.QVBoxLayout()  # Определение layout
        layout.addWidget(self.projects_list)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.back_button)

        self.setLayout(layout)
        self.projects_list.itemClicked.connect(self.item_clicked)
        self.refresh_button.clicked.connect(self.refresh_projects_list)
        self.back_button.clicked.connect(self.main_app.switch_to_main_menu)

    def item_clicked(self, item):
        self.selected_project_id = self.projects_list.row(item)
        self.main_app.switch_to_edit_project(self.selected_project_id)

    def refresh_projects_list(self):
        self.projects_list.clear()
        projects = self.db.get_all_projects()
        for project in projects:
            item = QtWidgets.QListWidgetItem(project[1])
            self.projects_list.addItem(item)

def main():
    app = QtWidgets.QApplication(sys.argv)
    view_projects = ViewProjects()
    view_projects.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()