from PyQt5.QtWidgets import (
    QWidget, QScrollArea, QVBoxLayout, QPushButton,
    QLineEdit, QComboBox, QHBoxLayout, QCompleter
)

from PyQt5.QtCore import Qt


class MaltsScrollArea(QWidget):
    def __init__(self, data_grid, manager):
        super().__init__()
        self.manager = manager
        self.data_grid = data_grid
        self.init_ui()

    def init_ui(self):
        font = self.font()
        font.setPointSize(10)
        self.window().setFont(font)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(2)

        self.widget = QWidget(self.scroll_area)
        self.vertical_box = QVBoxLayout(self.widget)
        self.vertical_box.setAlignment(Qt.AlignTop)
        self.vertical_box.setSpacing(15)

        add_malt_button = QPushButton("Add new malt")
        add_malt_button.clicked.connect(self.add_new_row)
        self.vertical_box.addWidget(add_malt_button)

        self.add_new_row()

        self.scroll_area.setWidget(self.widget)
        self.setFixedSize(400, 300)

        self.setLayout(QVBoxLayout(self))
        self.layout().addWidget(self.scroll_area)

    def add_new_row(self):
        horizontal_box = QHBoxLayout()
        line_edit = QLineEdit()
        combo_box = self.init_combo_box()
        remove_button = QPushButton("Remove")
        remove_button.clicked.connect(
            lambda _, horizontal_box=horizontal_box: self.remove_row(horizontal_box))

        horizontal_box.addWidget(line_edit)
        horizontal_box.addWidget(combo_box)
        horizontal_box.addWidget(remove_button)

        horizontal_box.setStretch(0, 1)
        horizontal_box.setStretch(1, 9)
        horizontal_box.setStretch(2, 1)

        self.vertical_box.addLayout(horizontal_box)

    def remove_row(self, horizontal_box):
        self.layout().removeItem(horizontal_box)

        for i in reversed(range(horizontal_box.count())):
            horizontal_box.itemAt(i).widget().setParent(None)
        horizontal_box.setParent(None)

    def init_combo_box(self):
        combo_box = QComboBox()
        combo_box.addItems(["TO BE ADDED"])

        combo_box.setEditable(True)
        combo_box.setInsertPolicy(QComboBox.NoInsert)
        combo_box.completer().setCompletionMode(QCompleter.PopupCompletion)

        return combo_box
