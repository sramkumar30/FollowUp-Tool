from commons import Commons
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from CalendarWindow import CalendarWindow


class FollowUp(QMainWindow):
    def __init__(self):
        super(FollowUp, self).__init__()
        self.setGeometry(150, 150, 500, 300)
        self.setWindowTitle("FollowUp")
        self.commons = Commons()
        self.init_ui()

    def init_ui(self):
        self.add = QtWidgets.QPushButton(self)
        self.add.setText("Add")
        self.add.clicked.connect(self.show_calendar)

        self.edit = QtWidgets.QPushButton(self)
        self.edit.setText("Edit")
        self.edit.move(100, 0)
        self.edit.clicked.connect(self.clicked)

        self.delete = QtWidgets.QPushButton(self)
        self.delete.setText("Delete")
        self.delete.move(200, 0)
        self.delete.clicked.connect(self.clicked)

    def clicked(self):
        print("Clicked")

    def show_calendar(self):
        self.calendar_window = CalendarWindow()

def window():
    app = QApplication(sys.argv)
    win = FollowUp()
    win.show()
    sys.exit(app.exec_())

window()
