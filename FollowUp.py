from commons import *
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
        self._table = Task(self)
        self.init_ui()

    def init_ui(self):
        self.add = QtWidgets.QPushButton(self)
        self.add.setText("Add")
        self.add.clicked.connect(self.add_task)

        self.edit = QtWidgets.QPushButton(self)
        self.edit.setText("Edit")
        self.edit.move(100, 0)
        self.edit.clicked.connect(self.edit_task)

        self.delete = QtWidgets.QPushButton(self)
        self.delete.setText("Delete")
        self.delete.move(200, 0)
        self.delete.clicked.connect(self.delete_task)

    def add_task(self):
        self.calendar_window = CalendarWindow()

    def edit_task(self):
        print("Printing Edit")
        if self._table.is_item_selected():
            _id, _timeval, _taskval = self._table.get_data()
            self.calendar_window = CalendarWindow(True, _id, _timeval, _taskval)
        else:
            pass

    def delete_task(self):
        print("Printing Delete")
        if self._table.is_item_selected():
            _id, _timeval, _taskval = self._table.get_data()
            self.commons.remove_task(_id)
        else:
            pass


def window():
    app = QApplication(sys.argv)
    win = FollowUp()
    win.show()
    sys.exit(app.exec_())

window()
