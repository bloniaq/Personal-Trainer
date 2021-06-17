from datetime import datetime as dt

class Weight:

    def __init__(self):
        self.measurements = []

    def add_measurement(self, date, weight):
        self.measurements.append((date, weight))
        self.measurements.sort()

    def avg_weight(self):
        return sum([m[1] for m in self.measurements]) / len(self.measurements)

    def get_measurements(self, start_date=dt(1, 1, 1), end_date=dt.now()):
        result = []
        for m in self.measurements:
            if m[0] >= start_date and m[0].day <= end_date.day:
                result.append(m)

        return result
