from datetime import datetime as dt


class Weight:
    """Class used for operations on weight measurements
    """

    def __init__(self):
        self.measurements = []

    def add_measurement(self, date, weight):
        """Add measurement to memory.

        :param date: datetime
            The date of measure
        :param weight: float
            The value of measure
        :return: None
        """
        self.measurements.append((date, weight))
        self.measurements.sort()

    def avg_weight(self, start_date=None, end_date=None):
        """Calculate average value of weight in provided date range.

        :param start_date: datetime
        :param end_date: datetime
        :return: float
        """
        measurements = self.get_measurements(start_date, end_date)
        print('measurements from get_measurements : ', measurements)
        for m in measurements:
            print(m)
        return sum([m[1] for m in measurements]) / len(measurements)

    def get_measurements(self, start_date=None, end_date=None, prec='day'):
        """Filter out measurements outside of date range.

        :param start_date: datetime
        :param end_date: datetime
        :param prec: str
            The precision of date range.
                'day' - include all measurements made till end of end_date
                day
                'hour' - include all measurements made till precisely end_date
        :return:
        """
        if start_date is None:
            start_date = dt(1, 1, 1)
        if end_date is None:
            end_date = dt.now()
        elif prec == 'day':
            end_date = end_date.replace(hour=23, minute=59)
        result = []
        for m in self.measurements:
            if m[0] >= start_date and m[0] < end_date:
                result.append(m)
        print('results: ', result)

        return result
