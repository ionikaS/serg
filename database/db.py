import sqlite3
from pathlib import Path


class Database:

    def __init__(self, db_path=None):

        self.db_path = str(
            Path(db_path) if db_path else Path(__file__).with_name("silent.db")
        )
        self._connection = None

        self.create_database()

    # =====================================

    def connect(self):

        """Return the shared SQLite connection used by repository code."""
        if self._connection is None:
            self._connection = sqlite3.connect(self.db_path)
            self._connection.execute("PRAGMA foreign_keys = ON")

        return self._connection

    def close(self):
        """Close the managed connection when the application shuts down."""
        if self._connection is not None:
            self._connection.close()
            self._connection = None

    def execute(self, sql, params=()):
        cursor = self.connect().execute(sql, params)
        self.connect().commit()
        return cursor

    def fetch_one(self, sql, params=()):
        return self.connect().execute(sql, params).fetchone()

    def fetch_all(self, sql, params=()):
        return self.connect().execute(sql, params).fetchall()

    def fetch_all_as_dicts(self, sql, params=()):
        cursor = self.connect().execute(sql, params)
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    # =====================================

    def create_database(self):

        connection = self.connect()

        connection.execute("""
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

        connection.execute("""
        CREATE TABLE IF NOT EXISTS albums(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            project_id INTEGER,

            title TEXT,

            genre TEXT,

            mood TEXT,

            description TEXT
        )
        """)

        connection.commit()

    def get_tracks(self):
        """Return tracks as dictionaries for existing non-repository callers."""
        # Local import avoids a module cycle during construction of ``database``.
        from repositories.track_repository import TrackRepository

        return TrackRepository(self).all_as_dicts()


database = Database()
