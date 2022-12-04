import sqlite3

class DB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def execute_fetch_one(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def execute_fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def __enter__(self):
        return self

    def __exit__(self):
        self.conn.close()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.execute(query)

    def delete_table(self, table_name):
        query = f"DROP TABLE {table_name}"
        self.execute(query)
    
    def insert_query(self, table_name, columns, values):
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.execute(query)
    
    def delete_query(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.execute(query)

    def update_query(self, table_name, columns, condition):
        query = f"UPDATE {table_name} SET {columns} WHERE {condition}"
        self.execute(query)
    
    def select_query(self, table_name, columns, condition):
        query = f"SELECT {columns} FROM {table_name} WHERE {condition}"
        return self.execute_fetch_all(query)