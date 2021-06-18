class Controller:

    def __init__(self, view, model):
        self.view = view
        self.weight = model
        self._create_view_callbacks()

    def _create_view_callbacks(self):
        functions = [('1', self.add_measurement),
                     ('2', self.show_measurements),
                     ('3', self.avg_weight)]
        for f in functions:
            self.view.add_callback(f[0], f[1])

    def add_measurement(self):
        date, weight = self.view.get_measurement()
        self.weight.add_measurement(date, weight)

    def show_measurements(self):
        start_date, end_date = self.view.get_date_range()
        measurements = self.weight.get_measurements(start_date, end_date)
        self.view.show_measurements(measurements)

    def avg_weight(self):
        avg_weight = self.weight.avg_weight()
        self.view.show_avg_weight(avg_weight)

    def run(self):
        return self.view.run()
