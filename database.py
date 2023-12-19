import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('project_management.db')
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.add_description_column()
    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS person (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS project (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                manager_id INTEGER,
                start_date TEXT,
                end_date TEXT,
                FOREIGN KEY(manager_id) REFERENCES person(id)
            )
        """)
        self.conn.commit()

    def add_user(self, username, password, role):
        self.cursor.execute("""
            INSERT INTO person (username, password, role) VALUES (?, ?, ?)
        """, (username, password, role))
        self.conn.commit()

    def get_user(self, username):
        self.cursor.execute("""
            SELECT * FROM person WHERE username = ?
        """, (username,))
        return self.cursor.fetchone()

    def add_project(self, name, description, manager_id, start_date, end_date):
        self.cursor.execute("""
            INSERT INTO project (name, description, manager_id, start_date, end_date) VALUES (?, ?, ?, ?, ?)
        """, (name, description, manager_id, start_date, end_date))
        self.conn.commit()

    def get_project(self, project_id):
        self.cursor.execute("""
            SELECT * FROM project WHERE id = ?
        """, (project_id,))
        return self.cursor.fetchone()

    def delete_project(self, project_id):
        self.cursor.execute("""
            DELETE FROM project WHERE id = ?
        """, (project_id,))
        self.conn.commit()
    def get_all_projects(self):
        self.cursor.execute("""
            SELECT * FROM project
        """)
        return self.cursor.fetchall()

    def update_project(self, project_id, name, description, manager_id, start_date, end_date):
        self.cursor.execute("""
            UPDATE project
            SET name = ?, description = ?, manager_id = ?, start_date = ?, end_date = ?
            WHERE id = ?
        """, (name, description, manager_id, start_date, end_date, project_id))
        self.conn.commit()

    def add_user(self, username, password, role):
        self.cursor.execute("""
            INSERT INTO person (username, password, role) VALUES (?, ?, ?)
        """, (username, password, role))
        self.conn.commit()

    def get_user_by_id(self, user_id):
        self.cursor.execute("""
            SELECT * FROM person WHERE id = ?
        """, (user_id,))
        return self.cursor.fetchone()

    def add_description_column(self):
        try:
            self.cursor.execute("""
                SELECT description FROM project LIMIT 1
            """)
        except sqlite3.OperationalError:
            self.cursor.execute("""
                ALTER TABLE project ADD COLUMN description TEXT NOT NULL
            """)
            self.conn.commit()