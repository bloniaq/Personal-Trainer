import trainer.application
import trainer.view.console
import trainer.view.desktop_tk
import trainer.controller
import trainer.models.weight
from datetime import datetime as dt


def test_three_measurements_console(capsys, monkeypatch):
    w1 = 99.9
    d1 = '2021.06.16 07:37'
    w2 = 101.2
    d2 = '2021.06.17 07:42'
    w3 = 102.3
    d3 = '2021.06.18 07:22'
    responses = iter(['1',
                      str(w1), d1,
                      '1',
                      str(w2), d2,
                      '1',
                      str(w3), d3,
                      '3', '', '',
                      '0'])
    w_list = [w1, w2, w3]
    monkeypatch.setattr('builtins.input', lambda value: next(responses))

    app = trainer.application.Application()
    view = trainer.view.console.ConsoleView()
    weight = trainer.models.weight.Weight()
    app.controller = trainer.controller.Controller(view, weight)
    app.run()

    captured = capsys.readouterr().out
    message = 'Average weight is {} kg'.format(str(round(
        sum(w_list) / len(w_list), 1)))
    assert message in captured

def test_add_measurement_desktop():
    app = trainer.application.Application()
    view = trainer.view.desktop_tk.DesktopView()
    weight = trainer.models.weight.Weight()
    app.controller = trainer.controller.Controller(view, weight)

    view.bld.var_msrment.set(140)
    view.bld.var_date.set('2021.06.16 07:37')
    app.controller.add_measurement()

    assert weight.measurements[0] == (dt(2021, 6, 16, 7, 37), 140)

def test_average_measurement_selection_desktop():
    app = trainer.application.Application()
    view = trainer.view.desktop_tk.DesktopView()
    weight = trainer.models.weight.Weight()
    app.controller = trainer.controller.Controller(view, weight)

    view.bld.var_msrment.set(160)
    view.bld.var_date.set('2021.06.16 07:37')
    app.controller.add_measurement()
    view.bld.var_msrment.set(110)
    view.bld.var_date.set('2021.08.16 08:37')
    app.controller.add_measurement()
    view.bld.var_msrment.set(120)
    view.bld.var_date.set('2021.04.16 09:37')
    app.controller.add_measurement()
    view.bld.var_msrment.set(150)
    view.bld.var_date.set('2021.07.16 09:37')
    app.controller.add_measurement()

    # Are measurements sorted
    assert weight.measurements[0] == (dt(2021, 4, 16, 9, 37), 120)

    # Average value of all
    app.controller.avg_weight()
    assert view.bld.lbl_reslin3.cget('text') == '135.0 kg'

    # Average value of last two records selected
    items = view.bld.trv_records.get_children()
    view.bld.trv_records.selection_set(items[1], items[2], items[3])
    app.controller.avg_weight()
    assert view.bld.lbl_reslin3.cget('text') == '140.0 kg'

