from repositories.base_repository import BaseRepository


class AlbumRepository(BaseRepository):

    def create(
        self,
        project_id,
        title,
        genre,
        mood,
        description=""
    ):

        cursor = self.execute(
            """
            INSERT INTO albums(
                project_id,
                title,
                genre,
                mood,
                description
            )
            VALUES(?, ?, ?, ?, ?)
            """,
            (
                project_id,
                title,
                genre,
                mood,
                description
            )
        )

        return cursor.lastrowid

    def all(self):

        return self.fetch_all(
            "SELECT * FROM albums ORDER BY id"
        )

    def by_id(self, album_id):

        return self.fetch_one(
            "SELECT * FROM albums WHERE id=?",
            (album_id,)
        )

    def delete(self, album_id):

        self.execute(
            "DELETE FROM albums WHERE id=?",
            (album_id,)
        )
