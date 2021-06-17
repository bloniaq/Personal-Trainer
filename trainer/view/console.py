from datetime import datetime as dt

DATEFORMAT = '%Y.%m.%d %H:%M'

class ConsoleView():

    def __init__(self):
        self.callbacks = {}

    def add_callback(self, key, method):
        self.callbacks[key] = method

    def run(self):
        while True:
            option = self._menu()
            if option == '0':
                break
            self.callbacks[option]()

        return option

    def get_measurement(self):
        print('\n# ADD MEASUREMENT')
        print('')
        weight = input('Enter the weight:\n')
        print('')
        date = input('Enter the date of measurement (YYYY.MM.DD HH:mm):\n')
        print('Measurement saved.')
        return (self._convert_date(date), float(weight))

    def get_date_range(self):
        # TODO: Implement case when user don't pass any date, or pass only one
        print('\nEnter date range')
        print('')
        start_date = input('Enter start date (YYYY.MM.DD):\n') + ' 00:00'
        print('')
        end_date = input('Enter end date (YYYY.MM.DD):\n') + ' 23:59'
        return (self._convert_date(start_date), self._convert_date(end_date))

    def show_measurements(self, measurements):
        # TODO: Add some title prints etc.
        for m in measurements:
            record = m[0].strftime(DATEFORMAT) + ':\t' + str(m[1]) + ' kg'
            print(record)

    def show_avg_weight(self, value):
        # TODO: Improve prints
        print('Average weight is {} kg'.format(str(round(value, 1))))

    def _menu(self):
        print('\n### MENU ###')
        print('')
        print('[1] Add Measurement')
        print('[2] Show Measurements')
        print('[3] Average Weight')
        print('[0] Exit Program\n')
        choice = input('Pick function\n')
        return choice

    def _convert_date(self, date_str):
        date = dt.strptime(date_str, DATEFORMAT)
        return date
