from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

import pickle
from os.path import exists, getsize
import datetime
import sys

#Define goon_count
global goon_count
goon_count =[]

#Get Todays Date
current_date = datetime.datetime.now()
if exists('save.pkl') and getsize('save.pkl') > 0:
    with open('save.pkl', 'rb') as file:
        goon_count = pickle.load(file)
else:
    with open('save.pkl', 'wb') as file:
        goon_count = [0,current_date - datetime.timedelta(seconds = 1200)]
        pickle.dump(goon_count, file)

class Window(QWidget):
    def __init__ (self, parent=None):
        super().__init__(parent)
        # Button with a parent widget
        self.setWindowTitle("goonstat")
        self.button = QPushButton(text="GOON!!!!!", parent=self)
        self.button.setFixedSize(500, 500)
        self.button.clicked.connect(self.goon_counts)
        
        if current_date - datetime.timedelta(minutes = 20) == goon_count[1]:
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)
            self.button.setText(f"You have gooned on the {goon_count[1]}")

        if str(current_date.month) + "-" + str(current_date.day) == "1-1":
            self.button.setText(f"You have gooned an amount of {goon_count[0]}")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def goon_counts(self): 
        goon_count[0] += 1
        goon_count[1] = current_date
        self.button.setText(f"You have gooned on the {goon_count[1]}")
        self.button.setEnabled(False) 
        if str(current_date.month) + "-" + str(current_date.day) == "1-2":
            goon_count[0] = 1
        with open('save.pkl', 'wb') as file:
            pickle.dump(goon_count, file)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show() 
    sys.exit(app.exec())       
