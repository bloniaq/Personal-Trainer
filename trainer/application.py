import trainer.view.console
import trainer.view.desktop_tk
import trainer.controller
import trainer.models.weight


class Application:

    def __init__(self):
        # view = trainer.view.console.ConsoleView()
        view = trainer.view.desktop_tk.DesktopView()
        model = trainer.models.weight.Weight()
        self.controller = trainer.controller.Controller(view, model)

    def run(self):
        self.controller.run()
