
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

import pickle

import sys


class Window(QWidget):
    def __init__ (self, parent=None):
        super().__init__(parent)
        # Button with a parent widget
        self.goon_count = 0
        self.setWindowTitle("goonstat")
        self.button = QPushButton(text="GOON!!!!!", parent=self)
        self.button.setFixedSize(100, 60)
        self.button.clicked.connect(self.goon_counts)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def save_goon_count(count):
        try:
            with open("data.pickle", "wb") as f:   
                pickle.dump(count, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            self.button.setText("UNABLE TO SAVE GOON")
            
    def goon_counts(self): 
        self.count += 1
        self.button.setText(f"goons = {goon_count}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show() 
    sys.exit(app.exec())       