from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QGridLayout, QLabel
)

from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import Qt, QRegExp


class CalculationsGrid(QWidget):
    """Widget consisting of gridlayout which shows all of the calculations of the recipe.

    Has also the volume change line edit.
    """

    def __init__(self, manager):
        """Constructor of the class.

        Args:
            manager (Manager_services): The manager_services class of the recipe.
        """
        super().__init__()
        self.manager = manager
        self.init_ui()

    def init_ui(self):
        """Initializes the widgets.
        """

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

        volume_header = QLabel("Volume:")
        line_edit = QLineEdit(volume)
        regex = QRegExp("[0-9]+(\\.[0-9]+)?")
        validator = QRegExpValidator(regex)
        line_edit.setValidator(validator)
        line_edit.textEdited.connect((
            lambda text: self.volume_changed(text)))
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
        """Updates all of the labels when an ingredient is changed.

        Args:
            new_values (list): A list consisting of the new values.
        """

        self.initial_values = new_values
        for index, value in enumerate(new_values):
            self.value_labels[index].setText(value)

    def volume_changed(self, text):
        """Handles the change of the volume line edit.

        Converts the value into float and passes it on to the manager.

        This should not receive incorrect inputs due to line edits validator but try/except keeps
        it safe in case of an unprepared inputs.

        Args:
            text (str): The user input in the volume line edit.
        """

        try:
            results = self.manager.volume_changed(float(text))
            self.update_values(results)
        except:
            pass
