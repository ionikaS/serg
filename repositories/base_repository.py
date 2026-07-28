import sqlite3


class BaseRepository:

    def __init__(self, connection):

        self.connection = connection

    def execute(self, sql, params=()):

        cursor = self.connection.cursor()

        cursor.execute(sql, params)

        self.connection.commit()

        return cursor

    def fetch_one(self, sql, params=()):

        cursor = self.connection.cursor()

        cursor.execute(sql, params)

        row = cursor.fetchone()

        return row

    def fetch_all(self, sql, params=()):

        cursor = self.connection.cursor()

        cursor.execute(sql, params)

        rows = cursor.fetchall()

        return rows