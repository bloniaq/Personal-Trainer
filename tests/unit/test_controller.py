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
        assert controller.model is not None
        assert controller.run is not None

    def test_console_run_start_and_exit(self, console_weight_controller,
                                        monkeypatch):
        controller = console_weight_controller
        monkeypatch.setattr('builtins.input', lambda value: '0')
        assert controller.run() == '0'

    def test_callbacks_console(self, console_weight_controller):
        controller = console_weight_controller
        assert controller.view.callbacks['1'] == controller.add_measurement

    def test_add_measuerement(self, console_weight_controller, monkeypatch):
        controller = console_weight_controller
        date = dt(2021, 5, 24, 6, 52)
        date_str = '2021.05.24 6:52'
        weight = '98.2'
        inputs = iter([weight, date_str])
        monkeypatch.setattr('builtins.input', lambda input: next(inputs))
        controller.add_measurement()
        assert controller.model.measurements[0][0] == date
        assert controller.model.measurements[0][1] == float(weight)

    def test_convert_date(self, console_weight_controller):
        controller = console_weight_controller
        date_str = '2021.05.24 6:52'
        date = dt(2021, 5, 24, 6, 52)
        assert controller._convert_date(date_str) == date

    def test_avg_weight(self, console_weight_controller, monkeypatch, capsys):
        controller = console_weight_controller
        date_1 = '2021.05.24 6:52'
        weight_1 = '98'
        date_2 = '2021.06.24 6:52'
        weight_2 = '100'
        inputs = iter([weight_1, date_1, weight_2, date_2])
        monkeypatch.setattr('builtins.input', lambda input: next(inputs))
        controller.add_measurement()
        controller.add_measurement()
        controller.avg_weight()
        message = 'Average weight is 99.0 kg'
        captured = capsys.readouterr().out
        assert message in captured
