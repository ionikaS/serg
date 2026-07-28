from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit
)


class AIDashboard(QWidget):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("""
        QWidget{
            background:#1B1F24;
            color:white;
        }

        QLabel{
            font-size:18px;
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
        """)

        layout = QVBoxLayout(self)

        title = QLabel("🧠 AI Dashboard")

        layout.addWidget(title)

        self.info = QTextEdit()

        self.info.setReadOnly(True)

        layout.addWidget(self.info)

    def show_dna(self, dna):

        text = ""

        text += "========== AI REPORT ==========\n\n"

        text += f"Genre : {dna.genre}\n"
        text += f"Mood : {dna.mood}\n"
        text += f"Lead : {dna.lead}\n"
        text += f"Support : {dna.support}\n"
        text += f"Key : {dna.key}\n"
        text += f"BPM : {dna.bpm}\n"
        text += f"Atmosphere : {dna.atmosphere}\n"
        text += f"Drums : {dna.drums}\n\n"

        text += "========== SCORES ==========\n\n"

        text += f"AI Score : {dna.ai_score}\n"
        text += f"Emotion : {dna.emotion}\n"
        text += f"Originality : {dna.originality}\n"
        text += f"Commercial : {dna.commercial}\n"
        text += f"Cinematic : {dna.cinematic}\n"
        text += f"Synergy : {dna.synergy}\n"
        text += f"Suno : {dna.suno}\n\n"

        text += "========== AI EXPLANATION ==========\n\n"

        for line in dna.explanation:

            text += "✓ " + line + "\n"

        self.info.setPlainText(text)