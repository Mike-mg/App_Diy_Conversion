# Widgets frames

import tkinter as tk
from tkinter import messagebox as messagebox


class FramesWidgets:
    # Class frames of program

    def __init__(self) -> None:

        self.bg = "#f28de2"
        self.dict_percent_dosage_aroma = {"aroma": self.selected_percent_aroma.get()}, {"base": 100}

# Command by quantity total ---------------------------------------------------

    def calcul_by_entry_quantity_total(self):

        try:

            if self.entry_value_entry_quantity_total.get() > 0:

                base = self.entry_value_entry_quantity_total.get() * self.dict_percent_dosage_aroma[1]["base"] / (self.dict_percent_dosage_aroma[0]["aroma"] + self.dict_percent_dosage_aroma[1]["base"])
                base = round(base, 1)
                aroma = base * self.selected_percent_aroma[0]["aroma"] / self.dict_percent_dosage_aroma[1]["base"]
                aroma = round(aroma, 1)
                self.value_show_quantity_total.set(self.entry_value_entry_quantity_total.get())
                self.value_show_aroma.set(aroma)
                self.value_show_base.set(base)

        except Exception:
            messagebox.showerror(
                title="Erreur de saisie",
                message="Erreur de saisie\nTous les champs non utilisés \
                    doivent être à 0.\nLes champs vont être réinitialisés") # noqa

# Command by aroma ------------------------------------------------------------

    def calcul_by_entry_aroma(self):

        try:
            if self.entry_aroma.get() > 0:

                base = self.entry_aroma.get() * self.dict_percent_dosage_aroma[1]["base"] / self.dict_percent_dosage_aroma[0]["aroma"]
                base = round(base, 1)
                self.value_show_quantity_total.set(base + self.entry_aroma.get())
                self.value_show_base.set(base)
                self.value_show_aroma.set(self.entry_aroma.get)

        except Exception:
            messagebox.showerror(title="Erreur de saisie",
            message="Erreur de saisie\nTous les champs non utilisés \
                doivent être à 0.\nLes champs vont être réinitialisés") # noqa

# Command by base -------------------------------------------------------------

    def calcul_by_base(self):

        try:

            if self.entry_base.get() > 0:

                aroma = self.dict_percent_dosage_aroma[0]["aroma"] * self.dict_percent_dosage_aroma[0]["aroma"] / self.dict_percent_dosage_aroma[0]["aroma"]
                aroma = round(aroma, 2)
                self.value_show_quantity_total.set(self.entry_base.get() + aroma)
                self.value_show_aroma.set(aroma)
                self.value_show_base.set(self.entry_base.get())

        except Exception:
            messagebox.showerror(
                title="Erreur de saisie",
                message="Erreur de saisie\nTous les champs non utilisés doivent être à 0.\nLes champs vont être réinitialisés") # noqa

# Frame percent aroma selected ------------------------------------------------

    def frame_percent_dosage_aroma(self, window) -> None:
        # Show frame percent dosage

        frame_selected_dosage = tk.Frame(
            window, borderwidth=2, relief="raised", bg=self.bg, border=3)

        frame_selected_dosage.grid(
            row=0, column=0, padx=(50, 0), pady=(50, 25))

        label_selected_dosage_aroma = tk.Label(
            frame_selected_dosage, text="Selected dosage")

        label_selected_dosage_aroma.config(bg=self.bg)

        label_selected_dosage_aroma.grid(
            row=0, column=0, padx=(0, 0), pady=(0, 0))

        self.selected_percent_aroma = tk.Scale(
            frame_selected_dosage, digits=2, length=375, from_=0, to=20,
            orient="horizontal", bg=self.bg, troughcolor="white",
            font=("Arial", 14), fg="white")

        self.selected_percent_aroma.grid(row=1, column=0)

# Frame quantity --------------------------------------------------------------

    def frame_quantity(self, window) -> None:
        # show frame quantity desired

        frame_quantity_total = tk.Frame(
            window, borderwidth=3, relief="raised", bg=self.bg)

        frame_quantity_total.grid(row=1, column=0, padx=(50, 0), pady=(0, 25))

        label_quantity_total = tk.Label(
            frame_quantity_total, text="Quantity total")

        label_quantity_total.config(
            width=35, justify="center", padx=2, pady=2, bg="#c8a6cb",
            relief="ridge", bd=2)

        label_quantity_total.grid(
            row=0, column=0, padx=(15, 15), pady=(15, 15))

        self.value_show_quantity_total = tk.DoubleVar()
        self.show_entry_quantity_total = tk.Label(
            frame_quantity_total,
            textvariable=self.value_show_quantity_total)

        self.show_entry_quantity_total.config(
            width=15, justify="center", padx=2, pady=2, bg="white",
            relief="ridge", bd=2)

        self.show_entry_quantity_total.grid(
            row=1, column=0, padx=(0, 0), pady=(0, 15))

        self.entry_value_entry_quantity_total = tk.DoubleVar()
        self.entry_entry_quantity_total = tk.Entry(
            frame_quantity_total,
            textvariable=self.entry_value_entry_quantity_total)

        self.entry_entry_quantity_total.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2)

        self.entry_entry_quantity_total.grid(
            row=0, column=1, padx=(0, 15), pady=(0, 0))

        button_entry_quantity_total = tk.Button(
            frame_quantity_total, text="Valid",
            command=self.calcul_by_entry_quantity_total)

        button_entry_quantity_total.place(x=334, y=50)

# Frame aroma -----------------------------------------------------------------

    def frame_aroma(self, window) -> None:
        # show frame quantity aroma

        frame_aroma = tk.Frame(
            window, borderwidth=3, relief="raised",
            padx=0, pady=0, bg=self.bg)

        frame_aroma.grid(row=2, column=0, padx=(50, 0), pady=(0, 25))

        label_aroma = tk.Label(frame_aroma, text="Quantity of aroma")

        label_aroma.config(width=35, justify="center", padx=2, pady=2,
                           bg="#c8a6cb", relief="ridge", bd=2)

        label_aroma.grid(row=0, column=0, padx=(15, 15), pady=(15, 10))

        self.value_show_aroma = tk.DoubleVar()
        self.show_aroma = tk.Label(
            frame_aroma, textvariable=self.value_show_aroma)

        self.show_aroma.config(
            width=15, justify="center", padx=2, pady=2, bg="white",
            relief="ridge", bd=2)

        self.show_aroma.grid(row=1, column=0, padx=(0, 0), pady=(0, 15))

        self.entry_value_aroma = tk.DoubleVar()
        self.entry_aroma = tk.Entry(
            frame_aroma, textvariable=self.entry_value_aroma)

        self.entry_aroma.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2)

        self.entry_aroma.grid(row=0, column=1, padx=(0, 15), pady=(0, 0))

        button_aroma = tk.Button(frame_aroma, text="Valid")
        button_aroma.place(x=334, y=50)

# Frame base ------------------------------------------------------------------

    def frame_base(self, window) -> None:
        # show frame quantity base

        frame_base = tk.Frame(
            window, borderwidth=3, relief="raised",
            padx=0, pady=0, bg=self.bg)

        frame_base.grid(row=3, column=0, padx=(50, 0), pady=(0, 0))

        base = tk.Label(frame_base, text="Quantity of base")

        base.config(width=35, justify="center", padx=2, pady=2, bg="#c8a6cb",
                    relief="ridge", bd=2)

        base.grid(row=0, column=0, padx=(15, 15), pady=(15, 10))

        self.value_show_base = tk.DoubleVar()
        self.show_base = tk.Label(
            frame_base, textvariable=self.value_show_base)

        self.show_base.config(
            width=15, justify="center", padx=2, pady=2, bg="white",
            relief="ridge", bd=2)

        self.show_base.grid(row=1, column=0, padx=(0, 0), pady=(0, 15))

        self.entry_value_base = tk.DoubleVar()
        self.entry_base = tk.Entry(frame_base, textvariable=self.entry_value_base)
        self.entry_base.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2)

        self.entry_base.grid(row=0, column=1, padx=(0, 15), pady=(0, 0))

        button_base = tk.Button(frame_base, text="Valid")
        button_base.place(x=334, y=50)
