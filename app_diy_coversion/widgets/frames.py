# Module Widgets frames

import tkinter as tk
from tkinter import messagebox as messagebox


class FramesWidgets:
    # Class frames of program

    def __init__(self) -> None:

        self.bg = "#f28de2"
        self.dict_base = {"base": 100}

# On clic button 1 mouse ------------------------------------------------------

    def clic_button_1_event(self, event):
        # Reset values on click mouse 1

        self.value_entry_quantity_total.set(0)
        self.value_show_quantity_total.set(0)

        self.value_entry_aroma.set(0)
        self.value_show_aroma.set(0)

        self.value_entry_base.set(0)
        self.value_show_base.set(0)

# function reset values -------------------------------------------------------

    def reset_values(self):
        # Reset values of main window

        self.selected_percent_aroma.set(0)

        self.value_entry_quantity_total.set(0)
        self.value_show_quantity_total.set(0)

        self.value_entry_aroma.set(0)
        self.value_show_aroma.set(0)

        self.value_entry_base.set(0)
        self.value_show_base.set(0)

# function command button by quantity total -----------------------------------

    def calcul_by_entry_quantity_total(self):
        # function of button command by quantity total

        try:

            if self.selected_percent_aroma.get() == 0:
                messagebox.showwarning(
                    title="Field invalid", message="Selected a percent aroma")

                self.reset_values()

            elif self.value_entry_quantity_total.get() > 0:

                base = self.value_entry_quantity_total.get() \
                    * self.dict_base["base"] \
                    / (self.selected_percent_aroma.get()
                        + self.dict_base["base"])

                base = round(base, 1)
                aroma = base * self.selected_percent_aroma.get() \
                    / self.dict_base["base"]

                aroma = round(aroma, 1)

                self.value_show_quantity_total.set(
                    self.value_entry_quantity_total.get())

                self.value_show_aroma.set(aroma)
                self.value_show_base.set(base)

        except TypeError:
            messagebox.showerror(
                title="Erreur de saisie",
                message="Input a number integer")

            self.reset_values()

        except tk.TclError:

            messagebox.showerror(
                title="Input error",
                message="Input a number integer")

            self.reset_values()

# function command button by aroma --------------------------------------------

    def calcul_by_entry_aroma(self):
        # function of button command by aroma

        try:

            if self.selected_percent_aroma.get() == 0:
                messagebox.showwarning(
                    title="Field invalid", message="Selected a percent aroma")

                self.reset_values()

            elif self.value_entry_aroma.get() > 0:

                base = self.value_entry_aroma.get() \
                    * self.dict_base["base"] \
                    / self.selected_percent_aroma.get()

                base = round(base, 1)
                self.value_show_quantity_total.set(
                    base + self.value_entry_aroma.get())

                self.value_show_base.set(base)
                self.value_show_aroma.set(self.value_entry_aroma.get())

        except TypeError:

            messagebox.showerror(
                title="Erreur de saisie",
                message="Input a number integer")

            self.reset_values()

        except tk.TclError:

            messagebox.showerror(
                title="Input error",
                message="Input a number integer")

            self.reset_values()

# function command button by base ---------------------------------------------

    def calcul_by_entry_base(self):
        # function of button command by base

        try:

            if self.selected_percent_aroma.get() == 0:
                messagebox.showwarning(
                    title="Field invalid", message="Selected a percent aroma")

                self.reset_values()

            elif self.value_entry_base.get() > 0:

                aroma = self.selected_percent_aroma.get() \
                    * self.value_entry_base.get() \
                    / self.dict_base["base"]

                aroma = round(aroma, 1)

                self.value_show_quantity_total.set(
                    self.value_entry_base.get() + aroma)

                self.value_show_aroma.set(aroma)
                self.value_show_base.set(self.value_entry_base.get())

        except TypeError:
            messagebox.showerror(
                title="Erreur de saisie",
                message="Input a number integer")

            self.reset_values()

        except tk.TclError:
            messagebox.showerror(
                title="Input error",
                message="Input a number integer")

            self.reset_values()

# Frame percent aroma selected ------------------------------------------------

    def frame_percent_aroma_selected(self, window) -> None:
        # Show frame percent aroma selected

        frame_selected_dosage = tk.Frame(
            window, borderwidth=2, relief="raised", bg=self.bg, border=3)

        frame_selected_dosage.grid(
            row=0, column=0, padx=(50, 0), pady=(50, 25))

        label_selected_dosage_aroma = tk.Label(
            frame_selected_dosage, text="Selected percent aroma")

        label_selected_dosage_aroma.config(bg=self.bg)

        label_selected_dosage_aroma.grid(
            row=0, column=0, padx=(0, 0), pady=(15, 0))

        self.selected_percent_aroma = tk.Scale(
            frame_selected_dosage, digits=2, length=375, from_=0, to=20,
            orient="horizontal", bg=self.bg, troughcolor="white",
            font=("Arial", 14), fg="white")

        self.selected_percent_aroma.grid(
            row=1, column=0, padx=(25, 25), pady=(0, 25))

# Frame quantity total --------------------------------------------------------

    def frame_quantity_total(self, window) -> None:
        # show frame quantity total

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

        self.value_show_quantity_total = tk.StringVar()
        self.show_quantity_total = tk.Label(
            frame_quantity_total,
            textvariable=self.value_show_quantity_total)

        self.show_quantity_total.config(
            width=15, justify="center", padx=2, pady=2, bg="white",
            relief="ridge", bd=2)

        self.show_quantity_total.grid(
            row=1, column=0, padx=(0, 0), pady=(0, 15))

        self.value_entry_quantity_total = tk.IntVar()
        self.entry_quantity_total = tk.Entry(
            frame_quantity_total,
            textvariable=self.value_entry_quantity_total)

        self.entry_quantity_total.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2)

        self.entry_quantity_total.grid(
            row=0, column=1, padx=(0, 15), pady=(0, 0))

        button_entry_quantity_total = tk.Button(
            frame_quantity_total, text="Valid",
            command=self.calcul_by_entry_quantity_total)

        button_entry_quantity_total.place(x=334, y=50)

        self.entry_quantity_total.bind("<1>", self.clic_button_1_event)

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

        self.value_show_aroma = tk.StringVar()
        self.show_aroma = tk.Label(
            frame_aroma, textvariable=self.value_show_aroma)

        self.show_aroma.config(
            width=15, justify="center", padx=2, pady=2, bg="white",
            relief="ridge", bd=2)

        self.show_aroma.grid(row=1, column=0, padx=(0, 0), pady=(0, 15))

        self.value_entry_aroma = tk.IntVar()
        self.entry_aroma = tk.Entry(
            frame_aroma, textvariable=self.value_entry_aroma)

        self.entry_aroma.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2)

        self.entry_aroma.grid(row=0, column=1, padx=(0, 15), pady=(0, 0))

        button_aroma = tk.Button(
            frame_aroma, text="Valid", command=self.calcul_by_entry_aroma)

        button_aroma.place(x=334, y=50)

        self.entry_aroma.bind("<1>", self.clic_button_1_event)

# Frame base ------------------------------------------------------------------

    def frame_base(self, window) -> None:
        # show frame base

        frame_base = tk.Frame(
            window, borderwidth=3, relief="raised",
            padx=0, pady=0, bg=self.bg)

        frame_base.grid(row=3, column=0, padx=(50, 0), pady=(0, 0))

        base = tk.Label(frame_base, text="Quantity of base")

        base.config(width=35, justify="center", padx=2, pady=2, bg="#c8a6cb",
                    relief="ridge", bd=2)

        base.grid(row=0, column=0, padx=(15, 15), pady=(15, 10))

        self.value_show_base = tk.StringVar()
        self.show_base = tk.Label(
            frame_base, textvariable=self.value_show_base)

        self.show_base.config(
            width=15, justify="center", padx=2, pady=2, bg="white",
            relief="ridge", bd=2)

        self.show_base.grid(row=1, column=0, padx=(0, 0), pady=(0, 15))

        self.value_entry_base = tk.IntVar()
        self.entry_base = tk.Entry(
            frame_base, textvariable=self.value_entry_base)
        self.entry_base.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2)

        self.entry_base.grid(row=0, column=1, padx=(0, 15), pady=(0, 0))

        button_base = tk.Button(
            frame_base, text="Valid", command=self.calcul_by_entry_base)
        button_base.place(x=334, y=50)

        self.entry_base.bind("<1>", self.clic_button_1_event)
