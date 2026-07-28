from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QScrollArea,
    QSizePolicy
)

from PySide6.QtCore import Qt

from core.career_engine import career_engine


class InfoCard(QFrame):

    def __init__(self, title, value):
        super().__init__()

        self.title = QLabel(title)
        self.value = QLabel(str(value))

        self.setMinimumHeight(120)

        self.setStyleSheet("""
            QFrame{
                background:#2B3138;
                border-radius:14px;
            }

            QLabel{
                color:white;
                border:none;
            }
        """)

        layout = QVBoxLayout(self)

        self.title.setStyleSheet("""
            font-size:14px;
            color:#AAB4BF;
        """)

        self.value.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
        """)

        layout.addStretch()
        layout.addWidget(self.title)
        layout.addWidget(self.value)
        layout.addStretch()

    def update_value(self, value):
        self.value.setText(str(value))


class AlbumCard(QFrame):

    def __init__(self, album, tracks):
        super().__init__()

        self.setMinimumHeight(100)

        self.setStyleSheet("""
            QFrame{
                background:#313842;
                border-radius:12px;
            }

            QLabel{
                color:white;
                border:none;
            }
        """)

        layout = QVBoxLayout(self)

        title = QLabel(album)

        title.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
        """)

        count = QLabel(f"{tracks} Tracks")

        count.setStyleSheet("""
            color:#AAB4BF;
            font-size:14px;
        """)

        layout.addWidget(title)
        layout.addWidget(count)


class CareerManager(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QWidget{
                background:#1B1F24;
                color:white;
            }
        """)

        root = QVBoxLayout(self)

        title = QLabel("🏆 Career Manager")

        title.setStyleSheet("""
            font-size:34px;
            font-weight:bold;
        """)

        subtitle = QLabel(
            "Complete Artist Career Overview"
        )

        subtitle.setStyleSheet("""
            color:#9AA4AF;
            font-size:15px;
        """)

        root.addWidget(title)
        root.addWidget(subtitle)

        root.addSpacing(20)

        row = QHBoxLayout()

        self.albumCard = InfoCard("Albums", "0")
        self.trackCard = InfoCard("Tracks", "0")
        self.scoreCard = InfoCard("Average AI", "0")
        self.genreCard = InfoCard("Favorite Genre", "-")

        row.addWidget(self.albumCard)
        row.addWidget(self.trackCard)
        row.addWidget(self.scoreCard)
        row.addWidget(self.genreCard)

        root.addLayout(row)

        root.addSpacing(20)

        discographyTitle = QLabel("Discography")

        discographyTitle.setStyleSheet("""
            font-size:26px;
            font-weight:bold;
        """)

        root.addWidget(discographyTitle)

        self.scroll = QScrollArea()

        self.scroll.setWidgetResizable(True)

        self.scroll.setFrameShape(QFrame.NoFrame)

        self.container = QWidget()

        self.albumLayout = QVBoxLayout(self.container)

        self.scroll.setWidget(self.container)

        root.addWidget(self.scroll)

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        self.refresh()

    def refresh(self):

        stats = career_engine.statistics()

        self.albumCard.update_value(
            stats["albums"]
        )

        self.trackCard.update_value(
            stats["tracks"]
        )

        self.scoreCard.update_value(
            stats["average_ai"]
        )

        self.genreCard.update_value(
            stats["favorite_genre"]
        )

        while self.albumLayout.count():

            item = self.albumLayout.takeAt(0)

            if item.widget():

                item.widget().deleteLater()

        for album, tracks in stats["discography"].items():

            self.albumLayout.addWidget(

                AlbumCard(

                    album,

                    tracks

                )

            )

        self.albumLayout.addStretch()