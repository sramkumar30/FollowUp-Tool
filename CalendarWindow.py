from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QCalendarWidget, QLineEdit, QTimeEdit
from PyQt5.QtCore import QTime, QDate
from commons import Commons


class CalendarWindow(QMainWindow):
    def __init__(self):
        super(CalendarWindow, self).__init__()
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("Calendar")
        self.reminder_data = {}
        self.commons = Commons()
        self.init_ui()

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
        self.text.setPlaceholderText("Enter Task Description")

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
        self.tedit.setTime(self.time.currentTime())
        self.tedit.move(5, 260)

    def clicked(self):
        print("Clicked")

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
            self.commons.add_task(self.reminder_data)
            self.close()

        except Exception as err:
            print(err)