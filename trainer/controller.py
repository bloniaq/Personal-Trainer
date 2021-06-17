from datetime import datetime as dt


class Controller:

    def __init__(self, view, model):
        self.view = view
        self.weight = model
        self._create_view_callbacks()

    def _create_view_callbacks(self):
        functions = [('1', self.add_measurement),
                     ('3', self.avg_weight)]
        for f in functions:
            self.view.add_callback(f[0], f[1])

    def _convert_date(self, date_str):
        day_str, hour_str = date_str.split(' ')
        year, month, day = day_str.split('.')
        hour, minute = hour_str.split(':')
        return dt(int(year), int(month), int(day), int(hour), int(minute))

    def add_measurement(self):
        date_str, weight_str = self.view.get_measurement()
        date = self._convert_date(date_str)
        weight = float(weight_str)
        self.weight.add_measurement(date, weight)

    def avg_weight(self):
        avg_weight = self.weight.avg_weight()
        self.view.show_avg_weight(avg_weight)

    def run(self):
        return self.view.run()
