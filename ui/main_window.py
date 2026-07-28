from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget
)

from ui.sidebar import SideBar
from ui.topbar import TopBar

from ui.dashboard import Dashboard
from ui.melody_dna import MelodyDNA
from ui.prompt_builder import PromptBuilder
from ui.track_library import TrackLibrary
from ui.career_manager import CareerManager


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Silent Crescendo Studio")
        self.resize(1400, 900)

        central = QWidget()
        self.setCentralWidget(central)

        rootLayout = QHBoxLayout(central)

        # ================= Sidebar =================

        self.sidebar = SideBar()
        rootLayout.addWidget(self.sidebar)

        # ================= Right =================

        rightWidget = QWidget()
        rightLayout = QVBoxLayout(rightWidget)

        self.topbar = TopBar()
        rightLayout.addWidget(self.topbar)

        self.stack = QStackedWidget()

        # ---------- Pages ----------

        self.dashboard = Dashboard()

        self.melodyDNA = MelodyDNA()

        self.promptBuilder = PromptBuilder()

        self.trackLibrary = TrackLibrary()

        self.careerManager = CareerManager()

        # ---------- Stack ----------

        self.stack.addWidget(self.dashboard)

        self.stack.addWidget(self.melodyDNA)

        self.stack.addWidget(self.promptBuilder)

        self.stack.addWidget(self.trackLibrary)

        self.stack.addWidget(self.careerManager)

        rightLayout.addWidget(self.stack)

        rootLayout.addWidget(rightWidget)

        # ================= Navigation =================

        self.sidebar.dashboardClicked.connect(
            self.show_dashboard
        )

        self.sidebar.melodyClicked.connect(
            self.show_melody
        )

        self.sidebar.promptClicked.connect(
            self.show_prompt
        )

        self.sidebar.trackLibraryClicked.connect(
            self.show_library
        )

        self.sidebar.careerClicked.connect(
            self.show_career
        )

        # ================= Melody → Prompt =================

        self.melodyDNA.promptGenerated.connect(
            self.receive_prompt
        )

        self.show_dashboard()

        self.setStyleSheet("""
            QMainWindow{
                background:#1B1F24;
            }
        """)

    # =========================================

    def show_dashboard(self):

        self.stack.setCurrentWidget(
            self.dashboard
        )

    def show_melody(self):

        self.stack.setCurrentWidget(
            self.melodyDNA
        )

    def show_prompt(self):

        self.stack.setCurrentWidget(
            self.promptBuilder
        )

    def show_library(self):

        self.trackLibrary.load_tracks()

        self.stack.setCurrentWidget(
            self.trackLibrary
        )

    def show_career(self):

        self.stack.setCurrentWidget(
            self.careerManager
        )

    # =========================================

    def receive_prompt(self, prompt):

        self.promptBuilder.set_prompt(prompt)

        self.stack.setCurrentWidget(
            self.promptBuilder
        )