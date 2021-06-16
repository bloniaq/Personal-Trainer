import trainer.view.console as cons

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
    monkeypatch.setattr('builtins.input', lambda input: next(inputs))
    assert view.get_measurement() == (date_str, weight)
