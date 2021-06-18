import pytest

import trainer.controller as ctrl
import trainer.view.console as cons
import trainer.models.weight as weight

from datetime import datetime as dt


class Test_Console:

    @pytest.fixture
    def console_weight_controller(self):
        view = cons.ConsoleView()
        model = weight.Weight()
        controller = ctrl.Controller(view, model)
        return controller

    def test_init(self, console_weight_controller):
        controller = console_weight_controller
        assert controller is not None
        assert controller.add_measurement is not None
        assert controller.avg_weight is not None
        assert controller.weight is not None
        assert controller.run is not None

    def test_console_run_start_and_exit(self, console_weight_controller,
                                        monkeypatch):
        controller = console_weight_controller
        monkeypatch.setattr('builtins.input', lambda value: '0')
        assert controller.run() == '0'

    def test_callbacks_console(self, console_weight_controller):
        controller = console_weight_controller
        assert controller.view.callbacks['1'] == controller.add_measurement

    def test_add_measurement(self, console_weight_controller, monkeypatch):
        controller = console_weight_controller
        date = dt(2021, 5, 24, 6, 52)
        date_str = '2021.05.24 6:52'
        weight_val = '98.2'
        inputs = iter([weight_val, date_str])
        monkeypatch.setattr('builtins.input', lambda inp: next(inputs))
        controller.add_measurement()
        assert controller.weight.measurements[0][0] == date
        assert controller.weight.measurements[0][1] == float(weight_val)

    def test_avg_weight(self, console_weight_controller, monkeypatch, capsys):
        controller = console_weight_controller
        date_1 = '2021.05.24 6:52'
        weight_1 = '97'
        date_2 = '2021.05.17 6:52'
        weight_2 = '101'
        inputs = iter([weight_1, date_1, weight_2, date_2, '', '', '', ''])
        monkeypatch.setattr('builtins.input', lambda inp: next(inputs))
        controller.add_measurement()
        controller.add_measurement()
        controller.avg_weight()
        message = 'Average weight is 99.0 kg'
        captured = capsys.readouterr().out
        print(captured)
        assert message in captured

    def test_show_measurements(self, console_weight_controller, monkeypatch,
                               capsys):
        controller = console_weight_controller
        measurements = [(dt(2021, 6, 10, 7, 53), 45.5),
                        (dt(2021, 6, 11, 9, 11), 45.3),
                        (dt(2021, 6, 12, 7, 45), 45.6),
                        (dt(2021, 6, 13, 7, 45), 46.2),
                        (dt(2021, 6, 14, 7, 36), 47.8),
                        (dt(2021, 6, 15, 8, 2), 46.9)]
        controller.weight.measurements = measurements
        start_date = '2021.06.12'
        end_date = '2021.06.14'
        inputs = iter([start_date, end_date, '', ''])
        monkeypatch.setattr('builtins.input', lambda inp: next(inputs))
        expected_outcome = '\n\n# MEASUREMENTS\n\n'\
                           '2021.06.12 07:45:\t45.6 kg\n' \
                           '2021.06.13 07:45:\t46.2 kg\n' \
                           '2021.06.14 07:36:\t47.8 kg'
        controller.show_measurements()
        captured = capsys.readouterr().out
        assert expected_outcome in captured
        controller.show_measurements()
        captured = capsys.readouterr().out
        expected_outcome_no_range = '\n\n# MEASUREMENTS\n\n' \
                                    '2021.06.10 07:53:\t45.5 kg\n' \
                                    '2021.06.11 09:11:\t45.3 kg\n' \
                                    '2021.06.12 07:45:\t45.6 kg\n' \
                                    '2021.06.13 07:45:\t46.2 kg\n' \
                                    '2021.06.14 07:36:\t47.8 kg\n' \
                                    '2021.06.15 08:02:\t46.9 kg'
        assert expected_outcome_no_range in captured

    def test_avg_weight_in_date_range(self, console_weight_controller,
                                      monkeypatch, capsys):
        controller = console_weight_controller
        measurements = [(dt(2021, 6, 10, 7, 53), 45.5),
                        (dt(2021, 6, 11, 9, 11), 45.3),
                        (dt(2021, 6, 12, 7, 45), 45.6),
                        (dt(2021, 6, 13, 7, 45), 46.2),
                        (dt(2021, 6, 14, 7, 36), 47.8),
                        (dt(2021, 6, 15, 8, 2), 46.9)]
        controller.weight.measurements = measurements
        start_date = '2021.06.12'
        end_date = '2021.06.14'
        inputs = iter([start_date, end_date])
        monkeypatch.setattr('builtins.input', lambda inp: next(inputs))
        expected_outcome = 'Average weight is 46.5 kg'
        controller.avg_weight()
        captured = capsys.readouterr().out
        assert expected_outcome in captured