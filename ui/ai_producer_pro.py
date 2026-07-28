from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QMessageBox
)

from core.brain import brain

from ui.live_ai_status import LiveAIStatus
from ui.ai_results_table import AIResultsTable
from ui.track_details import TrackDetails


class AIProducerPro(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("AI Producer Pro")

        self.setMinimumSize(1700, 900)

        self.setStyleSheet("""

        QWidget{

            background:#161A1F;
            color:white;

        }

        QPushButton{

            background:#3D7EFF;
            color:white;

            border:none;

            border-radius:8px;

            padding:12px;

            font-size:15px;

            font-weight:bold;

        }

        QPushButton:hover{

            background:#5A91FF;

        }

        """)

        self.tracks = []

        main = QHBoxLayout(self)

        # ==========================
        # LEFT
        # ==========================

        left = QVBoxLayout()

        self.generateButton = QPushButton(
            "🚀 AI Produce Top 10"
        )

        left.addWidget(
            self.generateButton
        )

        self.status = LiveAIStatus()

        left.addWidget(
            self.status
        )

        self.table = AIResultsTable()

        left.addWidget(
            self.table
        )

        # ==========================
        # RIGHT
        # ==========================

        self.details = TrackDetails()

        # ==========================

        main.addLayout(
            left,
            2
        )

        main.addWidget(
            self.details,
            3
        )

        # ==========================

        self.generateButton.clicked.connect(
            self.generate_tracks
        )

        self.table.trackSelected.connect(
            self.track_selected
        )

    # ==================================================

    def generate_tracks(self):

        self.generateButton.setEnabled(False)

        self.status.reset()

        def progress(

            current,

            total,

            best

        ):

            percent = int(
                current / total * 100
            )

            self.status.progress.setValue(
                percent
            )

            self.status.status.setText(
                f"Generating {current}/{total}"
            )

            self.status.best.setText(
                f"Best Score : {best}"
            )

            self.status.population.setText(
                f"Population : {total}"
            )

            self.status.generation.setText(
                "Evolution Running..."
            )

        try:

            self.tracks = brain.ai_produce(
                callback=progress
            )

            self.table.load_tracks(
                self.tracks
            )

            if self.tracks:

                self.details.show_track(
                    self.tracks[0]
                )

                self.status.finished(
                    self.tracks[0].ai_score
                )

        except Exception as e:

            QMessageBox.critical(

                self,

                "AI Producer",

                str(e)

            )

        self.generateButton.setEnabled(True)

    # ==================================================

    def track_selected(

        self,

        dna

    ):

        self.details.show_track(
            dna
        )