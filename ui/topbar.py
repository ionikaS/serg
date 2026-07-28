from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout
)

from PySide6.QtCore import Qt


class TopBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(90)

        layout = QHBoxLayout(self)

        # Ліва частина
        left = QVBoxLayout()

        title = QLabel("🎼 Silent Crescendo Studio")
        title.setStyleSheet("""
            color:white;
            font-size:24px;
            font-weight:bold;
        """)

        subtitle = QLabel("Professional AI Music Production Suite")
        subtitle.setStyleSheet("""
            color:#9AA4AF;
            font-size:12px;
        """)

        left.addWidget(title)
        left.addWidget(subtitle)

        layout.addLayout(left)

        layout.addStretch()

        # Права частина
        right = QVBoxLayout()

        status = QLabel("🟢 READY")
        status.setAlignment(Qt.AlignmentFlag.AlignRight)

        status.setStyleSheet("""
            color:#58D68D;
            font-size:14px;
            font-weight:bold;
        """)

        version = QLabel("Version 0.2 Alpha")
        version.setAlignment(Qt.AlignmentFlag.AlignRight)

        version.setStyleSheet("""
            color:#9AA4AF;
            font-size:11px;
        """)

        right.addWidget(status)
        right.addWidget(version)

        layout.addLayout(right)

        self.setStyleSheet("""
            background:#1F242B;
            border-radius:10px;
        """)