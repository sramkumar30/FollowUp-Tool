from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QCalendarWidget, QLineEdit, QTimeEdit
from PyQt5.QtCore import QTime, QDate
from commons import Commons


class CalendarWindow(QMainWindow):
    def __init__(self, update=False, id=None, timeval=None, taskval=None):
        super(CalendarWindow, self).__init__()
        self.setGeometry(300, 300, 400, 400)
        if update:
            self.setWindowTitle("Edit Task")
        else:
            self.setWindowTitle("Add Task")
        self.reminder_data = {}
        self.commons = Commons()
        self._id = id
        self._timeval = timeval
        self._taskval = taskval
        self.init_ui()
        self.update = update

    def init_ui(self):
        self.init_calendar()
        self.init_lineedit()
        self.init_pushbuttons()
        self.init_timedit()
        self.show()

    def init_calendar(self):
        try:
            self.date = QDate()
            self.calendar = QCalendarWidget(self)
            self.calendar.adjustSize()
            self.calendar.setMinimumDate(self.date.currentDate())
        except Exception as err:
            print(err)

    def init_lineedit(self):
        self.text = QLineEdit(self)
        self.text.setMaxLength(250)
        self.text.setGeometry(5,310,40,40)
        self.text.setFixedWidth(350)
        if not self.update:
            self._taskval = "Enter Task Description"
            self.text.setPlaceholderText(self._taskval)
        else:
            self.text.setText(self._taskval)

    def init_pushbuttons(self):
        self.OK = QtWidgets.QPushButton(self)
        self.OK.setText("OK")
        self.OK.move(195, 360)

        self.OK.clicked.connect(self.show_main)
        self.Cancel = QtWidgets.QPushButton(self)
        self.Cancel.setText("Cancel")
        self.Cancel.move(295, 360)
        self.Cancel.clicked.connect(self.close)

    def init_timedit(self):
        self.time = QTime()
        self.tedit = QTimeEdit(self)
        if not self.update:
            self._timeval = self.time.currentTime()
        else:
            self._timeval = QtCore.QTime.fromString(self._timeval, 'HH:mm:ss')
        self.tedit.setTime(self._timeval)
        self.tedit.move(5, 260)

    def show_main(self):
        try:
            selected_date = self.calendar.selectedDate()
            print(self.calendar.selectedDate())
            selected_time = self.tedit.time()
            print(selected_time.toString())
            print(self.text.text())
            self.reminder_data['Selected_Date'] = selected_date.toString()
            self.reminder_data['Selected_Time'] = selected_time.toString()
            self.reminder_data['Task_Description'] = self.text.text()
            print("From Calendar: ", self.reminder_data)
            if self.update:
                self.commons.prepare_json(self.reminder_data, self._id)
            else:
                self.commons.prepare_json(self.reminder_data)
            self.close()

        except Exception as err:
            print(err)