import trainer.application


def test_application_init():
    app = trainer.application.Application()
    assert app is not None
