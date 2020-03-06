import json


class Commons(object):
    def __init__(self) :
        self._config_json = r'config.json'
        self.load_file()

    def load_file(self):
        fileopen = False
        try:
            _jopen = open(self._config_json)
            self.reminder_data = json.load(_jopen)
            _jopen.close()
            fileopen = True
            print(self.reminder_data)
        except IOError:
            print("File not accessible")
        finally:
            if not fileopen:
                try:
                    _jopen = open(self._config_json,'w')
                    self.reminder_data = {'Selected_Date': {}, 'Selected_Time': {}, 'Task_Description': {}}
                    json.dump(self.reminder_data, _jopen)
                    _jopen.close()
                    print("Created new config file")
                except IOError:
                    print("Config file cannot be created")
            else:
                print("File Already exists. Skipping creation")

    def add_task(self, reminder_data):
        self._generateid()
        self.reminder_data['Selected_Date'].update({int(self._lst_row): reminder_data['Selected_Date']})
        self.reminder_data['Selected_Time'].update({int(self._lst_row): reminder_data['Selected_Time']})
        self.reminder_data['Task_Description'].update({int(self._lst_row): reminder_data['Task_Description']})
        print("From common module: ", self.reminder_data)
        self.write_json()

    def write_json(self):
        with open(self._config_json, 'w') as _jwrite:
            json.dump(self.reminder_data, _jwrite)
        _jwrite.close()

    def _generateid(self):
        _selected_date = self.reminder_data['Selected_Date']
        _all_keys = list(_selected_date.keys())
        _num_rows = len(_all_keys)
        if _num_rows > 0:
            self._lst_row = int(list(_selected_date.keys())[-1])
            self._lst_row += 1
        else:
            self._lst_row = 1

