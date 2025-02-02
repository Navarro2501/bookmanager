import sqlite3

class DatabaseConnection:
    def __init__(self, database_name):
        self.connection = None
        self.host = database_name

    def __enter__(self,):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
