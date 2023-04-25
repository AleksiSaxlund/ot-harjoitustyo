from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QGridLayout, QApplication
)

from ui import (
    malts_scroll_area, hops_scroll_area, yeasts_scroll_area,
    calculations_grid, notes_text_box
)
from entities.recipe import Recipe
from services.manager_services import ManagerServices


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.recipe = Recipe()
        self.manager = ManagerServices(self.recipe)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Homebrewing Calculator")
        self.setFixedSize(850, 720)

        # Setup layout
        main_widget = QWidget()
        main_layout = QGridLayout()
        main_widget.setLayout(main_layout)

        # Create class objects
        data_grid = calculations_grid.CalculationsGrid(self.manager)
        malts = malts_scroll_area.MaltsScrollArea(data_grid, self.manager)
        hops = hops_scroll_area.HopsScrollArea(data_grid, self.manager)
        yeasts = yeasts_scroll_area.YeastsScrollArea(data_grid, self.manager)
        notes = notes_text_box.NotesTextBox()

        # Add objects to main layout
        main_layout.addWidget(data_grid, 0, 0, 1, 0)
        main_layout.addWidget(malts, 1, 0)
        main_layout.addWidget(hops, 1, 1)
        main_layout.addWidget(yeasts, 2, 0)
        main_layout.addWidget(notes, 2, 1)

        self.setCentralWidget(main_widget)

# Run application


def run():
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()
