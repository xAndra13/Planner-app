import sys
from PySide6 import QtCore, QtWidgets, QtGui

class HomePanel(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.message = QtWidgets.QLabel(self, text="Hello!")
        self.button = QtWidgets.QPushButton(self, text = "Press me!")