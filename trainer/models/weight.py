class Weight:

    def __init__(self):
        self.measurements = []

    def add_measurement(self, date, weight):
        self.measurements.append((date, weight))

    def avg_weight(self):
        return sum([m[1] for m in self.measurements]) / len(self.measurements)

