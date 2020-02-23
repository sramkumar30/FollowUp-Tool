import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QMessageBox, QLineEdit, QTimeEdit
from PyQt5.QtCore import QTime



class FollowUp(QMainWindow):
    def __init__(self):
        super(FollowUp,self).__init__()
        self.setGeometry(150, 150, 500, 300)
        self.setWindowTitle("FollowUp")
        #self.showcalendar = CalendarPopUp()
        self.init_ui()

    def init_ui(self):
        self.add = QtWidgets.QPushButton(self)
        self.add.setText("Add")
        self.add.clicked.connect(self.show_calendar)
        #self.add.clicked.connect(self.clicked)

        self.edit = QtWidgets.QPushButton(self)
        self.edit.setText("Edit")
        self.edit.move(100,0)
        self.edit.clicked.connect(self.clicked)

        self.delete = QtWidgets.QPushButton(self)
        self.delete.setText("Delete")
        self.delete.move(200, 0)
        self.delete.clicked.connect(self.clicked)

    def list_tasks(self):
        pass

    def clicked(self):
        print("Clicked")

    def show_calendar(self):
        self.calendarPopUp = CalendarPopUp()
'''
    def show_calendar(self):
        msgbox = QMessageBox()
        #msgbox = CalendarPopUp()
        msgbox.setWindowTitle("Calendar")
        msgbox.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        #msgbox.setGeometry(300, 300, 200, 200)
        x = msgbox.exec_()
        #msgbox.show()
'''
'''
class CalendarPopUp(QDialog):
    def __init__(self):
        self._vbox = QVBoxLayout()
        self._calendar = QCalendarWidget()
        self._calendar.setWindowTitle("Calendar")
        self._vbox.addWidget(self._calendar)
        self.show()
'''
class CalendarPopUp(QMainWindow):
    def __init__(self):
        super(CalendarPopUp,self).__init__()
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("Calendar")
        self.init_ui()

    def init_ui(self):
        self.init_calendar()
        self.init_lineedit()
        self.init_pushbuttons()
        self.init_timedit()
        self.show()

    def init_calendar(self):
        self.calendar = QCalendarWidget(self)
        self.calendar.adjustSize()

    def init_lineedit(self):
        self.text = QLineEdit(self)
        self.text.setMaxLength(250)
        self.text.setGeometry(5,310,40,40)
        self.text.setFixedWidth(350)
        self.text.setPlaceholderText("Enter Task Description")

    def init_pushbuttons(self):
        self.OK = QtWidgets.QPushButton(self)
        self.OK.setText("OK")
        self.OK.move(195,360)
        self.Cancel = QtWidgets.QPushButton(self)
        self.Cancel.setText("Cancel")
        self.Cancel.move(295, 360)

    def init_timedit(self):
        self.time = QTime()
        self.tedit = QTimeEdit(self)
        self.tedit.setTime(self.time.currentTime())
        self.tedit.move(5,260)


        #self.text.move(200,300)




def window():
    app = QApplication(sys.argv)
    win = FollowUp()
    win.show()
    sys.exit(app.exec_())

window()
