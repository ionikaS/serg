from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton
)


class TrackDetails(QWidget):

    def __init__(self):

        super().__init__()

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

        QTextEdit{

            background:#252B33;

            color:white;

            border:1px solid #444;

            border-radius:8px;

            padding:8px;

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

        layout = QVBoxLayout(self)

        title = QLabel("🎵 Track Details")

        layout.addWidget(title)

        self.editor = QTextEdit()

        self.editor.setReadOnly(True)

        layout.addWidget(self.editor)

        self.copyButton = QPushButton("Copy Prompt")

        layout.addWidget(self.copyButton)

        self.copyButton.clicked.connect(

            self.copy_prompt

        )

    def show_track(

        self,

        dna

    ):

        text = ""

        text += "========== TRACK ==========\n\n"

        text += f"Genre : {dna.genre}\n"
        text += f"Mood : {dna.mood}\n"
        text += f"Lead : {dna.lead}\n"
        text += f"Support : {dna.support}\n"
        text += f"Key : {dna.key}\n"
        text += f"BPM : {dna.bpm}\n"
        text += f"Drums : {dna.drums}\n"
        text += f"Atmosphere : {dna.atmosphere}\n\n"

        text += "========== AI ==========\n\n"

        text += f"AI Score : {dna.ai_score}\n"
        text += f"Emotion : {dna.emotion}\n"
        text += f"Originality : {dna.originality}\n"
        text += f"Commercial : {dna.commercial}\n"
        text += f"Cinematic : {dna.cinematic}\n"
        text += f"Synergy : {dna.synergy}\n"
        text += f"Suno : {dna.suno}\n\n"

        text += "========== PROMPT ==========\n\n"

        text += dna.prompt

        text += "\n\n========== EXPLANATION ==========\n\n"

        for line in dna.explanation:

            text += "• " + line + "\n"

        self.editor.setPlainText(text)

    def copy_prompt(self):

        cursor = self.editor.textCursor()

        cursor.select(cursor.Document)

        self.editor.setTextCursor(cursor)

        self.editor.copy()