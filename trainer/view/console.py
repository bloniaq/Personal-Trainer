from datetime import datetime as dt

DATEFORMAT = '%Y.%m.%d %H:%M'


class ConsoleView:

    def __init__(self):
        self.callbacks = {}

    def add_callback(self, key, method):
        """Add a callback method with its key

        :param key: str
            The id key of function
        :param method: method
            The binded method
        :return: None
        """
        self.callbacks[key] = method

    def run(self):
        """Run menu loop

        :return: str
            option picked
        """
        while True:
            option = self._menu()
            if option == '0':
                break
            self.callbacks[option]()

        return option

    def get_measurement(self):
        """Get value of measurement and date of measure from user.

        :return: tuple
            Pair of date formatted by datetime and float value of weight
        """
        print('\n\n# ADD MEASUREMENT')
        weight = input('Enter the weight:\n')
        print('')
        date = input('Enter the date of measurement (YYYY.MM.DD HH:mm):\n')
        print('Measurement ({}: {}kg) saved.'.format(date, weight))
        return self._convert_date(date), float(weight)

    def get_date_range(self):
        """Get date range from user

        :return: tuple
            Pair of dates
        """
        print('\nEnter date range')
        print('')
        start_date = input('Enter start date (YYYY.MM.DD) or leave empty:\n')
        if start_date == '':
            start_date = None
        else:
            start_date += ' 00:00'
        print('')
        end_date = input('Enter end date (YYYY.MM.DD) or leave empty:\n')

        if end_date == '':
            end_date = None
        else:
            end_date += ' 23:59'
        print('Date range: START:{}\tEND:{}'.format(start_date, end_date))
        return self._convert_date(start_date), self._convert_date(end_date)

    def show_measurements(self, measurements):
        """Print measurements.

        :param measurements: list
            The list of measurements. Each element is a tuple of datetime
            formated date, and float value of measurement.
        :return: None
        """
        print('\n\n# MEASUREMENTS\n')
        for m in measurements:
            record = m[0].strftime(DATEFORMAT) + ':\t' + str(m[1]) + ' kg'
            print(record)

    def show_avg_weight(self, value):
        """Print calculated average weight.

        :param value: float
            The value to present
        :return:
        """
        print('\n\n# AVERAGE WEIGHT\n')
        print('\nAverage weight is {} kg'.format(str(round(value, 1))))

    def _menu(self):
        """Print menu content.

        :return: str
            Symbol of chosen function
        """
        print('\n### MENU ###')
        print('')
        print('[1] Add Measurement')
        print('[2] Show Measurements')
        print('[3] Average Weight')
        print('[0] Exit Program\n')
        choice = input('Pick function\n')
        return choice

    def _convert_date(self, date_str):
        """Convert input date to datetime format

        :param date_str: str
            The unformatted date
        :return: datetime or None
        """
        if date_str is not None:
            return dt.strptime(date_str, DATEFORMAT)
        else:
            return None
