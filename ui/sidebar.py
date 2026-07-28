from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)

from PySide6.QtCore import Signal, Qt


class SideBar(QWidget):

    dashboardClicked = Signal()
    melodyClicked = Signal()
    productionClicked = Signal()
    promptClicked = Signal()
    trackLibraryClicked = Signal()
    careerClicked = Signal()

    def __init__(self):
        super().__init__()

        self.setFixedWidth(260)

        self.setStyleSheet("""
            QWidget{
                background:#23272E;
            }

            QPushButton{
                background:#2D333B;
                color:white;
                border:none;
                border-radius:8px;
                padding:12px;
                font-size:15px;
                text-align:left;
            }

            QPushButton:hover{
                background:#3B424C;
            }

            QLabel{
                color:white;
            }
        """)

        layout = QVBoxLayout(self)

        title = QLabel("🎼 Silent Crescendo Studio")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
            padding-top:20px;
        """)

        subtitle = QLabel("Professional AI Music Production Suite")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("""
            color:#9AA4AF;
            font-size:11px;
            padding-bottom:20px;
        """)

        layout.addWidget(title)
        layout.addWidget(subtitle)

        self.dashboardButton = QPushButton("🏠 Dashboard")
        self.melodyButton = QPushButton("🧬 Melody DNA")
        self.productionButton = QPushButton("🎹 Production DNA")
        self.promptButton = QPushButton("🤖 Prompt Builder")
        self.libraryButton = QPushButton("🎵 Track Library")

        self.careerButton = QPushButton("🏆 Career Manager")

        self.albumButton = QPushButton("💿 Album Manager")
        self.coverButton = QPushButton("🖼 Cover Studio")
        self.shortsButton = QPushButton("🎬 Shorts Studio")
        self.analyticsButton = QPushButton("📈 Analytics")
        self.settingsButton = QPushButton("⚙ Settings")

        buttons = [

            self.dashboardButton,

            self.melodyButton,

            self.productionButton,

            self.promptButton,

            self.libraryButton,

            self.careerButton,

            self.albumButton,

            self.coverButton,

            self.shortsButton,

            self.analyticsButton,

            self.settingsButton

        ]

        for button in buttons:
            button.setMinimumHeight(45)
            layout.addWidget(button)

        layout.addStretch()

        self.dashboardButton.clicked.connect(
            self.dashboardClicked.emit
        )

        self.melodyButton.clicked.connect(
            self.melodyClicked.emit
        )

        self.productionButton.clicked.connect(
            self.productionClicked.emit
        )

        self.promptButton.clicked.connect(
            self.promptClicked.emit
        )

        self.libraryButton.clicked.connect(
            self.trackLibraryClicked.emit
        )

        self.careerButton.clicked.connect(
            self.careerClicked.emit
        )