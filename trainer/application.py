import trainer.view.console
import trainer.controller
import trainer.models.weight


class Application:

    def __init__(self):
        view = trainer.view.console.ConsoleView()
        model = trainer.models.weight.Weight()
        self.controller = trainer.controller.Controller(view, model)

    def run(self):
        self.controller.run()
