from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)


class AIResultsTable(QWidget):

    trackSelected = Signal(object)

    def __init__(self):

        super().__init__()

        self.tracks = []

        self.setStyleSheet("""

        QWidget{

            background:#1B1F24;

            color:white;

        }

        QLabel{

            font-size:20px;

            font-weight:bold;

            color:#8FC7FF;

        }

        QTableWidget{

            background:#252B33;

            color:white;

            border:1px solid #444;

            gridline-color:#333;

            selection-background-color:#3D7EFF;

        }

        QHeaderView::section{

            background:#2E3640;

            color:white;

            padding:6px;

            border:none;

        }

        """)

        layout = QVBoxLayout(self)

        title = QLabel("🏆 AI Producer Pro")

        layout.addWidget(title)

        self.table = QTableWidget()

        self.table.setColumnCount(8)

        self.table.setHorizontalHeaderLabels([

            "Rank",

            "Score",

            "Genre",

            "Mood",

            "Lead",

            "Support",

            "BPM",

            "Stars"

        ])

        self.table.horizontalHeader().setSectionResizeMode(

            QHeaderView.Stretch

        )

        layout.addWidget(self.table)

        self.table.cellClicked.connect(

            self.open_track

        )

    def load_tracks(

        self,

        tracks

    ):

        self.tracks = tracks

        self.table.setRowCount(

            len(tracks)

        )

        for row, dna in enumerate(tracks):

            self.table.setItem(

                row,

                0,

                QTableWidgetItem(

                    str(row + 1)

                )

            )

            self.table.setItem(

                row,

                1,

                QTableWidgetItem(

                    str(dna.ai_score)

                )

            )

            self.table.setItem(

                row,

                2,

                QTableWidgetItem(

                    dna.genre

                )

            )

            self.table.setItem(

                row,

                3,

                QTableWidgetItem(

                    dna.mood

                )

            )

            self.table.setItem(

                row,

                4,

                QTableWidgetItem(

                    dna.lead

                )

            )

            self.table.setItem(

                row,

                5,

                QTableWidgetItem(

                    dna.support

                )

            )

            self.table.setItem(

                row,

                6,

                QTableWidgetItem(

                    str(dna.bpm)

                )

            )

            stars = "★★★★★"

            if dna.ai_score < 99:

                stars = "★★★★☆"

            if dna.ai_score < 95:

                stars = "★★★☆☆"

            if dna.ai_score < 90:

                stars = "★★☆☆☆"

            if dna.ai_score < 80:

                stars = "★☆☆☆☆"

            self.table.setItem(

                row,

                7,

                QTableWidgetItem(

                    stars

                )

            )

    def open_track(

        self,

        row,

        column

    ):

        if row < len(self.tracks):

            self.trackSelected.emit(

                self.tracks[row]

            )