from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout
)


class TrackToolBar(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        self.addButton = QPushButton("➕ Add Track")
        self.editButton = QPushButton("✏ Edit")
        self.deleteButton = QPushButton("🗑 Delete")
        self.refreshButton = QPushButton("🔄 Refresh")

        buttons = [
            self.addButton,
            self.editButton,
            self.deleteButton,
            self.refreshButton
        ]

        for button in buttons:
            button.setMinimumHeight(42)
            button.setStyleSheet("""
                QPushButton{
                    background:#2D333B;
                    color:white;
                    border:none;
                    border-radius:8px;
                    padding:10px;
                    font-size:14px;
                    font-weight:bold;
                }

                QPushButton:hover{
                    background:#3B424C;
                }
            """)
            layout.addWidget(button)

        layout.addStretch()