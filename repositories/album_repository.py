from repositories.base_repository import BaseRepository


class AlbumRepository(BaseRepository):

    TABLE = "albums"

    def create(
        self,
        project_id,
        title,
        genre,
        mood,
        description="",
        cover="",
        release_date="",
        duration=0,
        average_ai_score=0,
        youtube_url="",
        spotify_url="",
        status="Draft"
    ):

        sql = f"""
        INSERT INTO {self.TABLE}
        (
            project_id,
            title,
            genre,
            mood,
            description,
            cover,
            release_date,
            duration,
            average_ai_score,
            youtube_url,
            spotify_url,
            status
        )
        VALUES
        (
            ?,?,?,?,?,?,?,?,?,?,?,?
        )
        """

        self.execute(
            sql,
            (
                project_id,
                title,
                genre,
                mood,
                description,
                cover,
                release_date,
                duration,
                average_ai_score,
                youtube_url,
                spotify_url,
                status
            )
        )

    def all(self):

        return self.fetch_all(

            f"SELECT * FROM {self.TABLE} ORDER BY id DESC"

        )

    def by_id(self, album_id):

        return self.fetch_one(

            f"SELECT * FROM {self.TABLE} WHERE id=?",

            (album_id,)

        )

    def delete(self, album_id):

        self.execute(

            f"DELETE FROM {self.TABLE} WHERE id=?",

            (album_id,)

        )

    def count(self):

        row = self.fetch_one(

            f"SELECT COUNT(*) FROM {self.TABLE}"

        )

        return row[0]

    def update_score(self, album_id, score):

        self.execute(

            f"""
            UPDATE {self.TABLE}

            SET average_ai_score=?

            WHERE id=?
            """,

            (score, album_id)

        )