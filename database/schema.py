SCHEMA = {

    "projects": [

        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("name", "TEXT NOT NULL"),
        ("description", "TEXT"),
        ("status", "TEXT"),
        ("created_at", "TEXT")

    ],

    "albums": [

        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("project_id", "INTEGER"),
        ("title", "TEXT"),
        ("genre", "TEXT"),
        ("mood", "TEXT"),
        ("description", "TEXT"),
        ("cover", "TEXT"),
        ("release_date", "TEXT"),
        ("duration", "INTEGER"),
        ("average_ai_score", "REAL"),
        ("youtube_url", "TEXT"),
        ("spotify_url", "TEXT"),
        ("status", "TEXT")

    ],

    "tracks": [

        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("album_id", "INTEGER"),
        ("track_number", "INTEGER"),
        ("title", "TEXT"),
        ("genre", "TEXT"),
        ("mood", "TEXT"),
        ("lead", "TEXT"),
        ("support", "TEXT"),
        ("bpm", "INTEGER"),
        ("musical_key", "TEXT"),
        ("duration", "INTEGER"),
        ("prompt", "TEXT"),
        ("ai_score", "REAL"),
        ("audio_file", "TEXT"),
        ("created_at", "TEXT")

    ],

    "covers": [

        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("album_id", "INTEGER"),
        ("track_id", "INTEGER"),
        ("image_file", "TEXT"),
        ("prompt", "TEXT"),
        ("style", "TEXT"),
        ("created_at", "TEXT")

    ],

    "shorts": [

        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT"),
        ("track_id", "INTEGER"),
        ("title", "TEXT"),
        ("hook", "TEXT"),
        ("description", "TEXT"),
        ("hashtags", "TEXT"),
        ("video_file", "TEXT"),
        ("published", "INTEGER")

    ]

}