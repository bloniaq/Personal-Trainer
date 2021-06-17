import pytest

import trainer.models.weight as weight
from datetime import datetime as dt

@pytest.fixture
def model_with_measurements():
    model = weight.Weight()
    measurements = [(dt(2021, 6, 12, 7, 45), 45.6),
                    (dt(2021, 6, 13, 7, 45), 46.2),
                    (dt(2021, 6, 14, 7, 36), 47.8),
                    (dt(2021, 6, 15, 8, 2), 46.9),
                    (dt(2021, 6, 11, 9, 11), 45.3),
                    (dt(2021, 6, 10, 7, 53), 45.5)]
    for m in measurements:
        model.add_measurement(m[0], m[1])
    return model

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

def test_avg_weight(model_with_measurements):
    model = model_with_measurements
    weight_sum = sum([m[1] for m in model.measurements])
    assert model.avg_weight() == weight_sum / len(model.measurements)

def test_get_measurements(model_with_measurements):
    model = model_with_measurements
    expected_all = [(dt(2021, 6, 10, 7, 53), 45.5),
                    (dt(2021, 6, 11, 9, 11), 45.3),
                    (dt(2021, 6, 12, 7, 45), 45.6),
                    (dt(2021, 6, 13, 7, 45), 46.2),
                    (dt(2021, 6, 14, 7, 36), 47.8),
                    (dt(2021, 6, 15, 8, 2), 46.9)]
    assert model.get_measurements() == expected_all
    expected_term = [(dt(2021, 6, 12, 7, 45), 45.6),
                     (dt(2021, 6, 13, 7, 45), 46.2),
                     (dt(2021, 6, 14, 7, 36), 47.8)]
    assert model.get_measurements(
        dt(2021, 6, 12), dt(2021, 6, 14)) == expected_term
