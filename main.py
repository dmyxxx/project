from PyQt6 import QtWidgets
import sys
from login import LoginScreen
from main_menu import MainMenu
from create_project import CreateProject
from view_projects import ViewProjects
from project_details import ProjectDetails
from edit_project import EditProject
from delete_project import DeleteProject
import database

class MainApp(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(MainApp, self).__init__(sys_argv)
        self.db = database.Database()
        self.login_screen = LoginScreen(self.db)
        self.main_menu = MainMenu(self.db, self)
        self.create_project = CreateProject(self, self.db)
        self.view_projects = ViewProjects(self.db,self)


        self.login_screen.login_button.clicked.connect(self.switch_to_main_menu)
        self.main_menu.new_project_button.clicked.connect(self.switch_to_create_project)
        self.main_menu.view_projects_button.clicked.connect(self.switch_to_view_projects)

        self.current_project_id = None

        self.init_ui()

    def load_styles(self):
        with open('styles.qss', 'r') as f:
            self.setStyleSheet(f.read())

    def init_ui(self):
        self.login_screen.show()
        self.load_styles()

    def switch_to_main_menu(self):
        self.login_screen.hide()
        self.main_menu.show()

    def switch_to_create_project(self):
        self.main_menu.hide()
        self.create_project.show()

    def switch_to_view_projects(self):
        self.main_menu.hide()
        self.view_projects.refresh_projects_list()
        self.view_projects.show()

    def switch_to_project_details(self, project_id):
        self.view_projects.hide()
        self.current_project_id = project_id
        project_details = ProjectDetails(project_id)
        project_details.show()

    def switch_to_edit_project(self, project_id):
        self.main_menu.hide()
        self.edit_project = EditProject(self.db, self, project_id)  # передаем project_id в EditProject
        self.edit_project.show()

    def switch_to_delete_project(self):
        self.main_menu.hide()
        self.delete_project = DeleteProject(self.db, self)  # создайте новый экземпляр DeleteProject
        self.delete_project.show()

    def refresh_view_projects(self):
        self.view_projects.refresh_projects_list()
        self.view_projects.show()



def main():
    app = MainApp(sys.argv)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

