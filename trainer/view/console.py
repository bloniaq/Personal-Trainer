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
        print('\n # ADD MEASUREMENT')
        print('')
        weight = input('Enter the weight:\n')
        print('')
        date = input('Enter the date of measurement (YYYY.MM.DD HH:mm):\n')
        print('Measurement saved.')
        return (date, weight)

    def show_avg_weight(self, value):
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
