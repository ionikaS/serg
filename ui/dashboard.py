from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
    QFrame
)

from PySide6.QtCore import Qt


class StatCard(QFrame):

    def __init__(self, title, value):
        super().__init__()

        self.setMinimumSize(240, 130)

        self.setStyleSheet("""
            QFrame{
                background:#252B33;
                border-radius:12px;
            }
        """)

        layout = QVBoxLayout(self)

        valueLabel = QLabel(str(value))
        valueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        valueLabel.setStyleSheet("""
            color:white;
            font-size:34px;
            font-weight:bold;
        """)

        titleLabel = QLabel(title)
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titleLabel.setStyleSheet("""
            color:#9AA4AF;
            font-size:14px;
        """)

        layout.addStretch()
        layout.addWidget(valueLabel)
        layout.addWidget(titleLabel)
        layout.addStretch()


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            background:#1B1F24;
        """)

        mainLayout = QVBoxLayout(self)

        title = QLabel("Dashboard")
        title.setStyleSheet("""
            color:white;
            font-size:32px;
            font-weight:bold;
            padding:10px;
        """)

        mainLayout.addWidget(title)

        grid = QGridLayout()

        grid.addWidget(StatCard("Tracks", 19), 0, 0)
        grid.addWidget(StatCard("Albums", 2), 0, 1)
        grid.addWidget(StatCard("Projects", 1), 1, 0)
        grid.addWidget(StatCard("Prompts", 148), 1, 1)

        mainLayout.addLayout(grid)
        mainLayout.addStretch()