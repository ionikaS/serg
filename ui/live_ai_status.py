from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QProgressBar
)


class LiveAIStatus(QWidget):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("""

        QWidget{
            background:#1B1F24;
            color:white;
        }

        QLabel{
            color:white;
            font-size:16px;
            font-weight:bold;
        }

        QProgressBar{

            border:1px solid #444;
            border-radius:8px;

            background:#252B33;

            text-align:center;

            height:22px;

        }

        QProgressBar::chunk{

            background:#3D7EFF;

            border-radius:8px;

        }

        """)

        layout = QVBoxLayout(self)

        self.title = QLabel("🤖 AI Evolution")

        layout.addWidget(self.title)

        self.status = QLabel("Waiting...")

        layout.addWidget(self.status)

        self.progress = QProgressBar()

        self.progress.setRange(0,100)

        self.progress.setValue(0)

        layout.addWidget(self.progress)

        self.best = QLabel("Best Score : --")

        layout.addWidget(self.best)

        self.population = QLabel("Population : --")

        layout.addWidget(self.population)

        self.generation = QLabel("Generation : --")

        layout.addWidget(self.generation)

    def reset(self):

        self.progress.setValue(0)

        self.status.setText("Generating...")

        self.best.setText("Best Score : --")

        self.population.setText("Population : --")

        self.generation.setText("Generation : --")

    def update_generation(

        self,

        generation,

        total,

        score,

        population

    ):

        percent = int(

            generation /

            total *

            100

        )

        self.progress.setValue(percent)

        self.status.setText(

            "AI Searching..."

        )

        self.best.setText(

            f"Best Score : {score}"

        )

        self.population.setText(

            f"Population : {population}"

        )

        self.generation.setText(

            f"Generation : {generation}/{total}"

        )

    def finished(

        self,

        score

    ):

        self.progress.setValue(100)

        self.status.setText(

            "Completed"

        )

        self.best.setText(

            f"Best Score : {score}"

        )