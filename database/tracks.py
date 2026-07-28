from database.db import database
from repositories.track_repository import TrackRepository


class TrackDatabase:

    def __init__(self, repository=None):
        self.repository = repository or TrackRepository(database)

    def add_track(
        self,
        title,
        album,
        genre,
        mood,
        bpm,
        musical_key,
        prompt,
        audio_file,
        cover_file,
        duration,
        created_at,
        status
    ):

        self.repository.create(
            title,
            album,
            genre,
            mood,
            bpm,
            musical_key,
            prompt,
            audio_file,
            cover_file,
            duration,
            created_at,
            status
        )

    def get_tracks(self):

        return self.repository.all()

    def delete_track(self, track_id):

        self.repository.delete(track_id)

    def update_track(
        self,
        track_id,
        title,
        album,
        genre,
        mood,
        bpm,
        musical_key,
        prompt,
        audio_file,
        cover_file,
        duration,
        status
    ):

        self.repository.update(
            title,
            album,
            genre,
            mood,
            bpm,
            musical_key,
            prompt,
            audio_file,
            cover_file,
            duration,
            status,
            track_id
        )


tracks = TrackDatabase()
