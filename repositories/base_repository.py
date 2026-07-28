from database.db import database


class BaseRepository:

    def __init__(self, connection=None):

        # Explicit connections remain supported for callers that own a transaction.
        self.connection = connection or database.connect()

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
