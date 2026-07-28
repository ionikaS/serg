from database.tracks import tracks

tracks.add_track(
    title="First Track",
    album="Album One",
    genre="Cinematic",
    mood="Emotional",
    bpm=72,
    musical_key="D Minor",
    prompt="Test Prompt",
    audio_file="audio/test.mp3",
    cover_file="covers/test.jpg",
    duration="05:12",
    created_at="2026-07-23",
    status="Ready"
)

print("Track added!")

all_tracks = tracks.get_tracks()

for track in all_tracks:
    print(track)