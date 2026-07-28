from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QTextEdit,
    QPushButton,
    QHBoxLayout
)


class AddTrackDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Track")
        self.resize(500, 500)

        layout = QVBoxLayout(self)

        form = QFormLayout()

        self.titleEdit = QLineEdit()
        self.albumEdit = QLineEdit()
        self.genreEdit = QLineEdit()
        self.moodEdit = QLineEdit()

        self.bpmEdit = QSpinBox()
        self.bpmEdit.setRange(40, 250)
        self.bpmEdit.setValue(72)

        self.keyEdit = QLineEdit()

        self.promptEdit = QTextEdit()

        form.addRow("Title", self.titleEdit)
        form.addRow("Album", self.albumEdit)
        form.addRow("Genre", self.genreEdit)
        form.addRow("Mood", self.moodEdit)
        form.addRow("BPM", self.bpmEdit)
        form.addRow("Key", self.keyEdit)
        form.addRow("Prompt", self.promptEdit)

        layout.addLayout(form)

        buttons = QHBoxLayout()

        self.saveButton = QPushButton("Save")
        self.cancelButton = QPushButton("Cancel")

        buttons.addStretch()
        buttons.addWidget(self.saveButton)
        buttons.addWidget(self.cancelButton)

        layout.addLayout(buttons)

        self.saveButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)