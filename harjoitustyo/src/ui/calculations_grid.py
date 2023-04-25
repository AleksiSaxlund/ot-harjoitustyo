from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QGridLayout, QLabel
)

from PyQt5.QtCore import Qt


class CalculationsGrid(QWidget):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.init_ui()

    def init_ui(self):
        font = self.font()
        font.setPointSize(10)
        self.window().setFont(font)

        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setHorizontalSpacing(50)
        layout.setVerticalSpacing(1)
        self.setLayout(layout)

        titles = ["OG:", "FG:", "ABV:", "SRM:", "IBU:"]
        initial_values = ["1.000", "1.000", "0.00%", "0", "0"]
        self.value_labels = []
        volume = "5"

        volume_header = QLabel("Volume")
        line_edit = QLineEdit(volume)
        line_edit.setMaximumWidth(50)
        layout.addWidget(volume_header, 0, 0)
        layout.addWidget(line_edit, 1, 0)

        for col in range(5):
            label = QLabel(f"{titles[col]}")
            layout.addWidget(label, 0, col+1)

            value_label = QLabel(f"{initial_values[col]}")
            layout.addWidget(value_label, 1, col+1)
            self.value_labels.append(value_label)

    def update_values(self, new_values):
        self.initial_values = new_values
        for index, value in enumerate(new_values):
            self.value_labels[index].setText(value)
