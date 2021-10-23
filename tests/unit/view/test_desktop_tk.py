import trainer.view.desktop_tk as d_view
import tkinter as tk

def test_init_desktop_view():
    view = d_view.DesktopView()
    view.run()
    assert view is not None
    assert isinstance(view.root, tk.Tk)

