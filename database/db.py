import sqlite3
import os


class Database:

    def __init__(self):

        self.db_path = os.path.join(
            "database",
            "silent.db"
        )

        self.create_database()

    # =====================================

    def connect(self):

        return sqlite3.connect(self.db_path)

    # =====================================

    def create_database(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tracks(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT,

            album TEXT,

            genre TEXT,

            mood TEXT,

            bpm INTEGER,

            musical_key TEXT,

            prompt TEXT,

            audio_file TEXT,

            cover_file TEXT,

            duration TEXT,

            created_at TEXT,

            status TEXT,

            ai_score REAL DEFAULT 0
        )
        """)

        connection.commit()

        connection.close()

    # =====================================

    def get_tracks(self):

        connection = self.connect()

        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()

        cursor.execute("""

            SELECT *

            FROM tracks

            ORDER BY id

        """)

        rows = cursor.fetchall()

        connection.close()

        return [

            dict(row)

            for row in rows

        ]


database = Database()