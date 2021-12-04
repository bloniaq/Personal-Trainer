import trainer.view.desktop_tk as d_view
import tkinter as tk
from datetime import datetime as dt


def test_init_desktop_view():
    view = d_view.DesktopView()
    view.run()
    assert view is not None
    assert isinstance(view.root, tk.Tk)

def test_get_measurement(monkeypatch):
    view = d_view.DesktopView()
    date_str = '2021.05.24 6:52'
    weight = '98.2'
    date = dt(2021, 5, 24, 6, 52)

    view.bld.var_msrment.set(weight)
    view.bld.var_date.set(date_str)

    assert view.get_measurement() == (date, float(weight))

def test_add_callbacks():
    view = d_view.DesktopView()

    def func():
        return 'success'

    view.add_callback('2', func)
    assert view.callbacks['2'] == func

def test_now_button():
    build = d_view.TkBuild()
    now = build.put_now_dt()
    assert build.var_date.get() == now

def test_convert_date():
    view = d_view.DesktopView()
    date_str = '2021.05.24 6:52'
    date = dt(2021, 5, 24, 6, 52)
    assert view._convert_date(date_str) == date

def test_show_measurements():
    view = d_view.DesktopView()
    measurements = [(dt(2021, 6, 10, 7, 53), 45.5),
                    (dt(2021, 6, 11, 9, 11), 45.3),
                    (dt(2021, 6, 12, 7, 45), 45.6),
                    (dt(2021, 6, 13, 7, 45), 46.2),
                    (dt(2021, 6, 14, 7, 36), 47.8),
                    (dt(2021, 6, 15, 8, 2), 46.9)]
    view.show_measurements(measurements)
    expected_outcome = '2021.06.10 07:53 45.5 kg \n' \
                       '2021.06.11 09:11 45.3 kg \n' \
                       '2021.06.12 07:45 45.6 kg \n' \
                       '2021.06.13 07:45 46.2 kg \n' \
                       '2021.06.14 07:36 47.8 kg \n' \
                       '2021.06.15 08:02 46.9 kg \n'
    tree = view.bld.trv_records
    content = ''
    for row_id in tree.get_children():
        row = tree.item(row_id)['values']
        line = ''
        for element in row:
            print(element)
            line += str(element) + ' '
        content += line + "\n"
    assert content == expected_outcome
