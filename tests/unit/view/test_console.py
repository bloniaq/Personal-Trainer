import trainer.view.console as cons
from datetime import datetime as dt

def test_init_console_view():
    view = cons.ConsoleView()
    assert view is not None
    assert type(view.callbacks) is dict

def test_menu_start_and_exit(monkeypatch):
    view = cons.ConsoleView()
    monkeypatch.setattr('builtins.input', lambda value: '0')
    assert view._menu() == '0'

def test_run_start_and_exit(monkeypatch):
    view = cons.ConsoleView()
    monkeypatch.setattr('builtins.input', lambda value: '0')
    assert view.run() == '0'

def test_add_callbacks():
    view = cons.ConsoleView()

    def func():
        return 'success'

    view.add_callback('2', func)
    assert view.callbacks['2'] == func

def test_get_measurement(monkeypatch):
    view = cons.ConsoleView()
    date_str = '2021.05.24 6:52'
    weight = '98.2'
    inputs = iter([weight, date_str])
    date = dt(2021, 5, 24, 6, 52)
    monkeypatch.setattr('builtins.input', lambda input: next(inputs))
    assert view.get_measurement() == (date, float(weight))

def test_get_date_range(monkeypatch):
    view = cons.ConsoleView()
    start_date_str = '2021.05.24'
    end_date_str = '2021.05.26'
    start_date = dt(2021, 5, 24, 0, 0)
    end_date = dt(2021, 5, 26, 23, 59)
    inputs = iter([start_date_str, end_date_str])
    monkeypatch.setattr('builtins.input', lambda input: next(inputs))
    assert view.get_date_range() == (start_date, end_date)

def test_convert_date():
    view = cons.ConsoleView()
    date_str = '2021.05.24 6:52'
    date = dt(2021, 5, 24, 6, 52)
    assert view._convert_date(date_str) == date

def test_show_measurements(capsys):
    view = cons.ConsoleView()
    measurements = [(dt(2021, 6, 10, 7, 53), 45.5),
                    (dt(2021, 6, 11, 9, 11), 45.3),
                    (dt(2021, 6, 12, 7, 45), 45.6),
                    (dt(2021, 6, 13, 7, 45), 46.2),
                    (dt(2021, 6, 14, 7, 36), 47.8),
                    (dt(2021, 6, 15, 8, 2), 46.9)]
    view.show_measurements(measurements)
    expected_outcome = '2021.06.10 07:53:\t45.5 kg\n' \
                       '2021.06.11 09:11:\t45.3 kg\n' \
                       '2021.06.12 07:45:\t45.6 kg\n' \
                       '2021.06.13 07:45:\t46.2 kg\n' \
                       '2021.06.14 07:36:\t47.8 kg\n' \
                       '2021.06.15 08:02:\t46.9 kg\n'
    assert capsys.readouterr().out == expected_outcome