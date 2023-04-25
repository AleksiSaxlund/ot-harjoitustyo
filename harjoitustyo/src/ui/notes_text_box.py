from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QTextEdit
)

from PyQt5.QtCore import Qt


class NotesTextBox(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        font = self.font()
        font.setPointSize(10)
        self.window().setFont(font)

        layout = QVBoxLayout()

        header = QLabel("Notes")
        header.setAlignment(Qt.AlignHCenter)
        layout.addWidget(header)

        text_box = QTextEdit()
        layout.addWidget(text_box)
        layout.setSpacing(10)
        self.setLayout(layout)
        self.setFixedSize(400, 283)
