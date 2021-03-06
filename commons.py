import json
from PyQt5 import QtWidgets


class Commons(object):
    def __init__(self):
        self._config_json = r'config.json'
        self._lst_row = None
        self.load_file()

    def get_json_data(self):
        return self._reminder_data

    def load_file(self):
        _fileopen = False
        try:
            _jopen = open(self._config_json)
            self._reminder_data = json.load(_jopen)
            _jopen.close()
            _fileopen = True
            print(self._reminder_data)
        except IOError:
            print("File not accessible")
        finally:
            if not _fileopen:
                try:
                    _jopen = open(self._config_json,'w')
                    self._reminder_data = {'Selected_Date': {}, 'Selected_Time': {}, 'Task_Description': {}}
                    json.dump(self._reminder_data, _jopen)
                    _jopen.close()
                    print("Created new config file")
                except IOError:
                    print("Config file cannot be created")
            else:
                print("File Already exists. Skipping creation")

    def prepare_json(self, _reminder_data, _id=None):
        #if _id is None then add entry to json else update an existing entry in json
        if _id is None:
            self._generateid()
        else:
            self._lst_row = _id
        self._reminder_data['Selected_Date'].update({int(self._lst_row): _reminder_data['Selected_Date']})
        self._reminder_data['Selected_Time'].update({int(self._lst_row): _reminder_data['Selected_Time']})
        self._reminder_data['Task_Description'].update({int(self._lst_row): _reminder_data['Task_Description']})
        print("From Add/Update module: ", self._reminder_data)
        self.write_json()

    def remove_task(self, _id):
        try:
            if (_id in self._reminder_data['Selected_Date'].keys()) and (_id in self._reminder_data['Selected_Time'].keys())and (_id in self._reminder_data['Task_Description'].keys()):
                self._reminder_data['Selected_Date'].pop(str(_id))
                self._reminder_data['Selected_Time'].pop(str(_id))
                self._reminder_data['Task_Description'].pop(str(_id))
                print("From Delete module: ", self._reminder_data)
                self.write_json()
            else:
                print("Id not found. Please check config file")
        except Exception as err:
            print("Exception in deleting task ", err)

    def write_json(self):
        with open(self._config_json, 'w') as _jwrite:
            json.dump(self._reminder_data, _jwrite)
        _jwrite.close()

    def _generateid(self):
        _selected_date = self._reminder_data['Selected_Date']
        _all_keys = list(_selected_date.keys())
        _num_rows = len(_all_keys)
        if _num_rows > 0:
            self._lst_row = int(list(_selected_date.keys())[-1])
            self._lst_row += 1
        else:
            self._lst_row = 1


class Task(object):
    def __init__(self, followup):
        self.table = QtWidgets.QTableWidget(followup)
        self._column_labels = ["Id", "Time", "Task"]
        self._item_clicked = False
        self.commons = Commons()
        self._header = self.table.horizontalHeader()
        self.init_table()
        self.load_data()

    def init_table(self):

        self.table.setColumnCount(3)
        self.table.move(20, 50)
        self.table.resize(400, 150)
        self.table.hideColumn(0)
        #self.table.hideRow(0)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(self._column_labels)
        self._header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self._header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.table.itemClicked.connect(self.print_data)
        self.load_data()
        self.table.show()

    def load_data(self):
        self.table.setRowCount(0)
        self._result = self.commons.get_json_data()

        print("Printing Json data in common window file: ")
        print(self._result)
        for rownum, rowdat in enumerate(self._result['Selected_Time']):
            data = []
            data.append(rowdat)
            _date_column = self._result['Selected_Date']
            _time_column = self._result['Selected_Time']
            _insert = "{} {}".format(_date_column[str(rowdat)], _time_column[str(rowdat)])
            data.append(_insert)
            _task_column = self._result['Task_Description']
            _insert = "{}".format(_task_column[str(rowdat)])
            data.append(_insert)
            self.table.insertRow(rownum)
            for column_num, dat in enumerate(data):
                print(data[column_num])
                self.table.setItem(rownum, column_num, QtWidgets.QTableWidgetItem(str(data[column_num])))

    def print_data(self):
        try:
            self._item_clicked = True
            self.table.selectRow(self.table.currentRow())
            _rownum = self.table.currentRow()
            _headercount = self.table.columnCount()
            for x in range(0, _headercount, 1):
                _headertext = self.table.horizontalHeaderItem(x).text()
                if _headertext == "Id":
                    self._cell = self.table.item(_rownum, x).text()# get cell at row, col
                    print(self._cell)
                    break
            self.get_data()
        except Exception as err:
            print(err)

    def is_item_selected(self):
        return self._item_clicked

    def get_data(self):
        try:
            _jsondata = self.commons.get_json_data()
            return str(self._cell), _jsondata['Selected_Time'][str(self._cell)], _jsondata['Task_Description'][str(self._cell)]

        except Exception as err:
            print(err)