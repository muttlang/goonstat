#import mysql.connector

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget


import sys

class Window(QWidget):
    def __init__ (self, parent=None):
        super().__init__(parent)
        # Button with a parent widget
        self.count = 0 
        self.button = QPushButton(text="GOON!!!!!", parent=self)
        self.button.setFixedSize(100, 60)
        self.button.clicked.connect(self.count_clicks)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)
    def count_clicks(self): 
        self.count += 1
        self.button.setText(f"goons = {self.count}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show() 
    sys.exit(app.exec())       