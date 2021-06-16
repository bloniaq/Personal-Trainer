import trainer.models.weight as weight
from datetime import datetime as dt

def test_init():
    model = weight.Weight()
    assert model is not None
    assert model.add_measurement is not None
    assert model.measurements is not None

def test_add_measurement():
    model = weight.Weight()
    date = dt(2021, 6, 16, 7, 45)
    weight_val = 45.6
    model.add_measurement(date, weight_val)
    assert model.measurements[0][0] == date
    assert model.measurements[0][1] == weight_val

def test_avg_weight():
    model = weight.Weight()
    measurements = [(dt(2021, 6, 16, 7, 45), 45.6),
                    (dt(2021, 6, 17, 7, 45), 46.2),
                    (dt(2021, 6, 18, 7, 45), 45.8),]
    for m in measurements:
        model.add_measurement(m[0], m[1])

    weight_sum = sum([m[1] for m in measurements])
    assert model.avg_weight() == weight_sum / len(measurements)
