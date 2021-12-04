import tkinter as tk
from tkinter import ttk
from datetime import datetime as dt

DATEFORMAT = '%Y.%m.%d %H:%M'


class DesktopView:

    def __init__(self):
        self.bld = TkBuild()
        self.root = self.bld.root
        self.callbacks = {}

    def add_callback(self, key, method):
        """Add a callback method with its key

        :param key: str
            The id key of function
        :param method: method
            The binded method
        :return: None
        """
        self.callbacks[key] = method

    def run(self):
        self.root.mainloop()

    def get_measurement(self):
        """Get value of measurement and date of measure from user.

        :return: tuple
            Pair of date formatted by datetime and float value of weight
        """
        weight = self.bld.var_msrment.get()
        date = self.bld.var_date.get()
        return self._convert_date(date), float(weight)

    def show_measurements(self, measurements):
        """Print measurements.

        :param measurements: list
            The list of measurements. Each element is a tuple of datetime
            formated date, and float value of measurement.
        :return: None
        """
        self.bld.trv_records.delete(* self.bld.trv_records.get_children())
        for m in measurements:
            date_str = m[0].strftime(DATEFORMAT)
            value_str = str(m[1]) + ' kg'
            self.bld.trv_records.insert("", 'end', values=[date_str, value_str])

    def _convert_date(self, date_str):
        """Convert input date to datetime format

        :param date_str: str
            The unformatted date
        :return: datetime or None
        """
        if date_str is not None:
            return dt.strptime(date_str, DATEFORMAT)
        else:
            return None


class TkBuild:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Personal Trainer")
        self.rootframe = tk.Frame(self.root)
        self.rootframe.pack(padx=10,pady=10)

        # Frames
        self.frm_msrment = tk.Frame(self.rootframe, height=180, width=300)
        self.frm_results = tk.Frame(self.rootframe, relief="sunken",
                                    borderwidth=1, height=180, width=200)
        self.frm_navi = tk.Frame(self.rootframe, height=200, width=200)
        self.frm_msrment.grid_propagate(0)
        self.frm_msrment.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        # self.frm_results.place(height=700, width=20, anchor="c")
        self.frm_results.grid_propagate(0)
        self.frm_results.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        self.frm_navi.grid_propagate(0)
        self.frm_navi.grid(row=1, column=1, padx=10, pady=10, sticky="se")

        # Treeview
        columns = ('id', 'date', 'msrment')
        self.trv_records = ttk.Treeview(self.rootframe, columns=columns,
                                        show='headings')
        self.trv_records.heading('id', text="ID")
        self.trv_records.column('id', width=50)
        self.trv_records.heading('date', text="Data Pomiaru")
        self.trv_records.column('date', width=150, anchor="e")
        self.trv_records.heading('msrment', text="Pomiar (kg)")
        self.trv_records.column('msrment', width=100)
        self.trv_records.grid(row=1, column=0)

        # Frame: Measurement
        self.frm_msrment_inn = tk.Frame(self.frm_msrment)
        # self.frm_msrment_inn.grid(row=0, column=0, padx=10, pady=10)
        self.frm_msrment_inn.place(in_=self.frm_msrment, anchor="c", relx=.5,
                                   rely=.5)

        self.var_msrment = tk.StringVar()
        self.var_date = tk.StringVar()

        self.lbl_msrdate1 = tk.Label(self.frm_msrment_inn, text="Data Pomiaru")
        self.lbl_msrdate2 = tk.Label(self.frm_msrment_inn, text="YYYY.MM.DD GG:mm")
        self.ent_msrdate = tk.Entry(self.frm_msrment_inn, width=15,
                                    textvariable=self.var_date)
        self.lbl_msrval = tk.Label(self.frm_msrment_inn, text="Pomiar (kg)")
        self.ent_msrval = tk.Entry(self.frm_msrment_inn, width=15)
        self.lbl_msrdate1.grid(row=0, column=0)
        self.lbl_msrdate2.grid(row=1, column=0)
        self.ent_msrdate.grid(row=2, column=0)
        self.lbl_msrval.grid(row=3, column=0)
        self.ent_msrval.grid(row=4, column=0)

        self.btn_now = tk.Button(self.frm_msrment_inn, text="Teraz",
                                 command=self.put_now_dt)
        self.btn_now.grid(row=2, column=1)

        self.btn_addmsrment = tk.Button(self.frm_msrment_inn, width=10,
                                        text="Dodaj\nPomiar", height=8)
        self.btn_addmsrment.grid(row=0, column=2, rowspan=5, padx=(10, 0))

        # Frame Results
        self.frm_results_inn = tk.Frame(self.frm_results)
        self.frm_results_inn.place(in_=self.frm_results, anchor="c", relx=.5,
                                   rely=.5)
        self.lbl_reslin1 = tk.Label(self.frm_results_inn)
        self.lbl_reslin2 = tk.Label(self.frm_results_inn)
        self.lbl_reslin3 = tk.Label(self.frm_results_inn, font=(
            "Arial", "20", "bold"
        ))
        self.lbl_reslin4 = tk.Label(self.frm_results_inn)

        # test
        self.lbl_reslin1.config(text='Testowy tekst')
        self.lbl_reslin2.config(text='Testowy tekst')
        self.lbl_reslin3.config(text='Testowy tekst')
        self.lbl_reslin4.config(text='Testowy tekst')

        self.lbl_reslin1.grid(row=0, column=0)
        self.lbl_reslin2.grid(row=1, column=0)
        self.lbl_reslin3.grid(row=2, column=0)
        self.lbl_reslin4.grid(row=3, column=0)

        # Frame Navigation
        self.frm_navi_inn = tk.Frame(self.frm_navi)
        self.frm_navi_inn.place(in_=self.frm_navi, anchor="c", relx=.5,
                                rely=.5)
        self.btn_delmsrment = tk.Button(self.frm_navi_inn, width=20, height=2,
                                        text="Usuń Pomiar")
        self.btn_delmsrment.grid(row=0, column=0)
        self.btn_avgweight = tk.Button(self.frm_navi_inn, width=20, height=2,
                                       text="Średnia Waga")
        self.btn_avgweight.grid(row=1, column=0)

    def put_now_dt(self):
        now = dt.now().strftime(DATEFORMAT)
        self.var_date.set(now)
        return now
