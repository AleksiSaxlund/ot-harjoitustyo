from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QTextEdit
)

from PyQt5.QtCore import Qt


class NotesTextBox(QWidget):
    """Widget that has the textbox for the notes.
    """

    def __init__(self):
        """Constructor of the class.
        """

        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initializes the widgets of the widget.
        """

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
        self.setFixedSize(475, 283)
