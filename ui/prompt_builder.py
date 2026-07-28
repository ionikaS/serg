from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
    QApplication
)


class PromptBuilder(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QWidget{
                background:#1B1F24;
                color:white;
            }

            QTextEdit{
                background:#252B33;
                color:white;
                border:1px solid #444;
                border-radius:8px;
                font-size:14px;
            }

            QPushButton{
                background:#3D7EFF;
                color:white;
                border:none;
                border-radius:8px;
                padding:12px;
                font-size:15px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#5A91FF;
            }
        """)

        layout = QVBoxLayout(self)

        title = QLabel("🤖 Prompt Builder")

        title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
            padding:10px;
        """)

        layout.addWidget(title)

        self.editor = QTextEdit()

        layout.addWidget(self.editor)

        self.copyButton = QPushButton("📋 Copy Prompt")

        layout.addWidget(self.copyButton)

        self.copyButton.clicked.connect(self.copy_prompt)

    def set_prompt(self, text):

        self.editor.setPlainText(text)

    def get_prompt(self):

        return self.editor.toPlainText()

    def copy_prompt(self):

        QApplication.clipboard().setText(
            self.editor.toPlainText()
        )