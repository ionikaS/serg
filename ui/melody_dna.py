from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QComboBox,
    QSpinBox,
    QTextEdit,
    QPushButton,
    QHBoxLayout
)

from PySide6.QtCore import Signal

from core.brain import brain

from core.music_constants import (
    GENRES,
    MOODS,
    LEAD_INSTRUMENTS,
    SUPPORT_INSTRUMENTS,
    DRUMS,
    ATMOSPHERES,
    ENERGY,
    KEYS
)


class MelodyDNA(QWidget):

    promptGenerated = Signal(str)

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
        QWidget{
            background:#1B1F24;
            color:white;
        }

        QComboBox,
        QSpinBox,
        QTextEdit{
            background:#252B33;
            color:white;
            border:1px solid #444;
            border-radius:6px;
            padding:6px;
        }

        QPushButton{
            background:#3D7EFF;
            color:white;
            border:none;
            border-radius:8px;
            padding:10px;
            font-weight:bold;
        }

        QPushButton:hover{
            background:#5A91FF;
        }
        """)

        main = QVBoxLayout(self)

        title = QLabel("🧬 Melody DNA Builder")
        title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
        """)

        main.addWidget(title)

        grid = QGridLayout()

        self.genre = QComboBox()
        self.genre.addItems(GENRES)

        self.mood = QComboBox()
        self.mood.addItems(MOODS)

        self.instrument = QComboBox()
        self.instrument.addItems(LEAD_INSTRUMENTS)

        self.secondInstrument = QComboBox()
        self.secondInstrument.addItem("Auto")
        self.secondInstrument.addItems(SUPPORT_INSTRUMENTS)

        self.energy = QComboBox()
        self.energy.addItems(ENERGY)

        self.key = QComboBox()
        self.key.addItems(KEYS)

        self.drums = QComboBox()
        self.drums.addItems(DRUMS)

        self.atmosphere = QComboBox()
        self.atmosphere.addItems(ATMOSPHERES)

        self.bpm = QSpinBox()
        self.bpm.setRange(40, 180)
        self.bpm.setValue(72)

        rows = [

            ("Genre", self.genre),

            ("Mood", self.mood),

            ("Lead Instrument", self.instrument),

            ("Second Instrument", self.secondInstrument),

            ("Energy", self.energy),

            ("Key", self.key),

            ("Drums", self.drums),

            ("Atmosphere", self.atmosphere),

            ("BPM", self.bpm)

        ]

        for row, (text, widget) in enumerate(rows):

            grid.addWidget(QLabel(text), row, 0)
            grid.addWidget(widget, row, 1)

        main.addLayout(grid)

        self.prompt = QTextEdit()
        self.prompt.setPlaceholderText("Generated prompt...")
        main.addWidget(self.prompt)

        buttons = QHBoxLayout()

        self.generateButton = QPushButton("Generate")

        self.aiButton = QPushButton("✨ AI Produce")

        self.copyButton = QPushButton("Copy")

        buttons.addWidget(self.generateButton)
        buttons.addWidget(self.aiButton)
        buttons.addWidget(self.copyButton)

        main.addLayout(buttons)

        self.scoreLabel = QLabel("AI Score: -- / 100")
        self.scoreLabel.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
            color:#6FD16F;
            padding-top:10px;
        """)

        main.addWidget(self.scoreLabel)

        self.reasonLabel = QLabel("AI Recommendation: --")
        self.reasonLabel.setWordWrap(True)
        self.reasonLabel.setStyleSheet("""
            color:#AFC7FF;
            padding:6px;
        """)

        main.addWidget(self.reasonLabel)

        self.generateButton.clicked.connect(
            self.generate_prompt
        )

        self.aiButton.clicked.connect(
            self.ai_produce
        )

        self.copyButton.clicked.connect(
            self.copy_prompt
        )
    def copy_prompt(self):

        self.prompt.selectAll()
        self.prompt.copy()

    def generate_prompt(self):

        data = {

            "genre": self.genre.currentText(),

            "mood": self.mood.currentText(),

            "lead": self.instrument.currentText(),

            "second": self.secondInstrument.currentText(),

            "energy": self.energy.currentText(),

            "key": self.key.currentText(),

            "drums": self.drums.currentText(),

            "atmosphere": self.atmosphere.currentText(),

            "bpm": self.bpm.value()

        }

        dna = brain.create_track(data)

        self.prompt.setPlainText(
            dna.prompt
        )

        self.scoreLabel.setText(
            f"AI Score: {dna.ai_score} / 100"
        )

        self.reasonLabel.setText(
            dna.reason
        )

        self.promptGenerated.emit(
            dna.prompt
        )

    def ai_produce(self):

        dna = brain.ai_produce()

        self.genre.setCurrentText(
            dna.genre
        )

        self.mood.setCurrentText(
            dna.mood
        )

        self.instrument.setCurrentText(
            dna.lead
        )

        if dna.support:

            index = self.secondInstrument.findText(
                dna.support
            )

            if index >= 0:

                self.secondInstrument.setCurrentIndex(
                    index
                )

        self.energy.setCurrentText(
            dna.energy
        )

        self.key.setCurrentText(
            dna.key
        )

        self.drums.setCurrentText(
            dna.drums
        )

        self.atmosphere.setCurrentText(
            dna.atmosphere
        )

        self.bpm.setValue(
            dna.bpm
        )

        self.prompt.setPlainText(
            dna.prompt
        )

        self.scoreLabel.setText(
            f"AI Score: {dna.ai_score} / 100"
        )

        self.reasonLabel.setText(
            dna.reason
        )

        self.promptGenerated.emit(
            dna.prompt
        )