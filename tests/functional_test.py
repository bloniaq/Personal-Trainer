import trainer.application
import trainer.view.console
import trainer.controller
import trainer.models.weight

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
                      '3',
                      '0'])
    w_list = [w1, w2, w3]
    monkeypatch.setattr('builtins.input', lambda value: next(responses))

    app = trainer.application.Application()
    view = trainer.view.console.ConsoleView()
    model = trainer.models.weight.Weight()
    app.controller = trainer.controller.Controller(view, model)
    app.run()

    captured = capsys.readouterr().out
    message = 'Average weight is {} kg'.format(str(round(
        sum(w_list) / len(w_list), 1)))
    assert message in captured
