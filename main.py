import sys
from interfaces.home import HomePanel
from PySide6 import QtCore, QtWidgets, QtGui

INIT_WIDTH = 1200
INIT_HEIGHT = 900

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAnimated(True)
        self.current_panel = HomePanel()
        self.setCentralWidget(self.current_panel)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = Window()
    window.resize(INIT_WIDTH, INIT_HEIGHT)
    window.show()

    sys.exit(app.exec())
