# Database Schema

## projects

| Field | Type |
|--------|------|
| id | INTEGER PK |
| name | TEXT |
| description | TEXT |
| status | TEXT |
| created_at | DATETIME |

---

## albums

| Field | Type |
|--------|------|
| id | INTEGER PK |
| project_id | INTEGER FK |
| title | TEXT |
| genre | TEXT |
| mood | TEXT |
| description | TEXT |
| cover | TEXT |
| release_date | TEXT |
| duration | INTEGER |
| average_ai_score | REAL |
| youtube_url | TEXT |
| spotify_url | TEXT |
| status | TEXT |

---

## tracks

| Field | Type |
|--------|------|
| id | INTEGER PK |
| album_id | INTEGER FK |
| track_number | INTEGER |
| title | TEXT |
| genre | TEXT |
| mood | TEXT |
| lead | TEXT |
| support | TEXT |
| bpm | INTEGER |
| musical_key | TEXT |
| duration | INTEGER |
| prompt | TEXT |
| ai_score | REAL |
| audio_file | TEXT |
| created_at | DATETIME |

---

## covers

| Field | Type |
|--------|------|
| id | INTEGER PK |
| album_id | INTEGER FK |
| track_id | INTEGER FK |
| image_file | TEXT |
| prompt | TEXT |
| style | TEXT |
| created_at | DATETIME |

---

## shorts

| Field | Type |
|--------|------|
| id | INTEGER PK |
| track_id | INTEGER FK |
| title | TEXT |
| hook | TEXT |
| description | TEXT |
| hashtags | TEXT |
| video_file | TEXT |
| published | INTEGER |

---

## prompts

| Field | Type |
|--------|------|
| id | INTEGER PK |
| track_id | INTEGER FK |
| version | INTEGER |
| prompt | TEXT |
| ai_score | REAL |
| created_at | DATETIME |

---

## analytics

| Field | Type |
|--------|------|
| id | INTEGER PK |
| album_id | INTEGER FK |
| track_id | INTEGER FK |
| platform | TEXT |
| views | INTEGER |
| likes | INTEGER |
| comments | INTEGER |
| watch_time | REAL |
| ctr | REAL |
| retention | REAL |
| updated_at | DATETIME |

---

## learning

| Field | Type |
|--------|------|
| id | INTEGER PK |
| dna_hash | TEXT |
| genre | TEXT |
| mood | TEXT |
| lead | TEXT |
| support | TEXT |
| average_score | REAL |
| best_score | REAL |
| uses | INTEGER |