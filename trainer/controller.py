import trainer.view.desktop_tk


class Controller:

    def __init__(self, view, weight):
        """

        :param view: View
        :param weight: Weight
        """
        self.view = view
        self.weight = weight
        self._create_view_callbacks()

    def _create_view_callbacks(self):
        """Add callbacks of self methods to the view

        :return: None
        """
        functions = [('1', self.add_measurement),
                     ('2', self.show_measurements),
                     ('3', self.avg_weight)]
        for f in functions:
            self.view.add_callback(f[0], f[1])

        self.view.bind_actions()

    def add_measurement(self):
        """Add a measurement

        :return: None
        """
        date, weight = self.view.get_measurement()
        self.weight.add_measurement(date, weight)
        if isinstance(self.view, trainer.view.desktop_tk.DesktopView):
            self.show_measurements()

    def show_measurements(self):
        """Print the measurements taken in the time period

        :return: None
        """
        start_date, end_date = self.view.get_date_range()
        measurements = self.weight.get_measurements(start_date, end_date)
        self.view.show_measurements(measurements)
        return start_date, end_date, measurements

    def avg_weight(self):
        """Print average weight for the time period

        :return: None
        """
        start_date, end_date = self.view.get_date_range()
        avg_weight = self.weight.avg_weight(start_date, end_date)
        self.view.show_avg_weight(avg_weight)

    def run(self):
        """Run the application

        :return: method
        """
        return self.view.run()
