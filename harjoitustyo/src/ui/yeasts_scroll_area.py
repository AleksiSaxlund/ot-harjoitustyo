from PyQt5.QtWidgets import (
    QWidget, QScrollArea, QVBoxLayout, QPushButton,
    QComboBox, QHBoxLayout, QCompleter
)

from PyQt5.QtCore import Qt


class YeastsScrollArea(QWidget):
    def __init__(self, data_grid, manager):
        super().__init__()
        self.manager = manager
        self.data_grid = data_grid
        self.all_yeasts = self.manager.get_all_yeasts()
        self.init_ui()

    def init_ui(self):
        # Set custom font size
        font = self.font()
        font.setPointSize(10)
        self.window().setFont(font)

        # Setup widget
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(2)

        self.widget = QWidget(self.scroll_area)
        self.vertical_box = QVBoxLayout(self.widget)
        self.vertical_box.setAlignment(Qt.AlignTop)
        self.vertical_box.setSpacing(15)

        # Setup add button and add to widget
        add_malt_button = QPushButton("Add new Yeast")
        add_malt_button.clicked.connect(self.add_new_row)
        self.vertical_box.addWidget(add_malt_button)

        # Create first row
        self.add_new_row()

        # Add widget to self layout
        self.scroll_area.setWidget(self.widget)
        self.setFixedSize(400, 300)

        self.setLayout(QVBoxLayout(self))
        self.layout().addWidget(self.scroll_area)

    # Adds new row to the scroll area
    def add_new_row(self):
        # Create objects
        horizontal_box = QHBoxLayout()
        combo_box = self.init_combo_box()
        remove_button = QPushButton("Remove")
        remove_button.setMaximumWidth(60)
        remove_button.clicked.connect(
            lambda _, horizontal_box=horizontal_box: self.remove_row(horizontal_box))

        # Add objects to layout
        horizontal_box.addWidget(combo_box)
        horizontal_box.addWidget(remove_button)

        # Add layout to scroll area
        self.vertical_box.addLayout(horizontal_box)

    def remove_row(self, horizontal_box):
        # Removes the ingredient from the recipe
        index = self.get_row(horizontal_box)
        values = self.manager.ingredient_removed(index, "yeasts")
        self.data_grid.update_values(values)

        # Remove layout
        self.layout().removeItem(horizontal_box)

        # Fix widget parents
        for i in reversed(range(horizontal_box.count())):
            horizontal_box.itemAt(i).widget().setParent(None)
        horizontal_box.setParent(None)

    def get_row(self, horizontal_box):
        # Returns the index of the horizontal box on the vertical box
        for i in range(self.vertical_box.count()):
            item = self.vertical_box.itemAt(i)
            if item.layout() == horizontal_box:
                return i - 1

    def init_combo_box(self):
        # Create object
        combo_box = QComboBox()
        combo_box.setMaximumWidth(275)
        combo_box.addItems([yeast.name for yeast in self.all_yeasts])
        combo_box.activated.connect(self.combo_box_signal)

        # Setup combo box
        combo_box.setEditable(True)
        combo_box.setInsertPolicy(QComboBox.NoInsert)
        combo_box.completer().setCompletionMode(QCompleter.PopupCompletion)

        return combo_box

    def combo_box_signal(self, index):
        values = self.manager.ingredient_added(
            self.all_yeasts[index], "yeasts")
        self.data_grid.update_values(values)
