from datetime import datetime as dt


class Weight:

    def __init__(self):
        self.measurements = []

    def add_measurement(self, date, weight):
        self.measurements.append((date, weight))
        self.measurements.sort()

    def avg_weight(self, start_date=None, end_date=None):
        measurements = self.get_measurements(start_date, end_date)
        return sum([m[1] for m in measurements]) / len(measurements)

    def get_measurements(self, start_date=None, end_date=None, prec='day'):
        if start_date is None:
            start_date = dt(1, 1, 1)
        if end_date is None:
            end_date = dt.now()
        elif prec == 'day':
            end_date = end_date.replace(hour=23, minute=59)
        result = []
        for m in self.measurements:
            if m[0] > start_date and m[0] < end_date:
                result.append(m)

        return result
