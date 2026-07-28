from repositories.album_repository import AlbumRepository


class AlbumService:

    def __init__(self, connection):

        self.repository = AlbumRepository(connection)

    def create_album(

        self,

        project_id,

        title,

        genre,

        mood,

        description=""

    ):

        self.repository.create(

            project_id=project_id,

            title=title,

            genre=genre,

            mood=mood,

            description=description

        )

    def albums(self):

        return self.repository.all()

    def album(self, album_id):

        return self.repository.by_id(album_id)

    def remove(self, album_id):

        self.repository.delete(album_id)