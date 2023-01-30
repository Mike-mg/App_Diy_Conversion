# Widgets frames

import tkinter as tk
import pkg_functions_utils


class FramesWidgets:
    # Class frames of program

    def __init__(self) -> None:
        self.bg = "#f28de2"

        self.selected_percent_dosage = 0
        self.entry_quantity_desired = 0
        self.entry_aroma = 0
        self.entry_base = 0

        self.show_quantity_desired = 0
        self.show_aroma = 0
        self.show_base = 0

# Frame dosage ----------------------------------------------------------------

    def frame_dosage(self, window) -> None:
        # Show frame percent dosage

        frame_selected_dosage = tk.Frame(
            window, borderwidth=2, relief="raised", bg=self.bg, border=3)

        frame_selected_dosage.grid(
            row=0, column=0, padx=(50, 0), pady=(50, 25))

        label_selected_dosage = tk.Label(
            frame_selected_dosage, text="Selected dosage")

        label_selected_dosage.config(bg=self.bg)

        label_selected_dosage.grid(row=0, column=0, padx=(0, 0), pady=(0, 0))

        selected_percent_dosage = tk.Scale(
            frame_selected_dosage, digits=2, length=375, from_=0, to=20,
            orient="horizontal", bg=self.bg, troughcolor="white",
            font=("Arial", 14), fg="white")

        selected_percent_dosage.grid(row=1, column=0)

        self.selected_percent_dosage = selected_percent_dosage.get()

# Frame quantity --------------------------------------------------------------

    def frame_quantity(self, window) -> None:
        # show frame quantity desired

        frame_quantity_desired = tk.Frame(
            window, borderwidth=3, relief="raised", bg=self.bg)

        frame_quantity_desired.grid(
            row=1, column=0, padx=(50, 0), pady=(0, 25))

        label_quantity_desired = tk.Label(
            frame_quantity_desired, text="Quantity total")

        label_quantity_desired.config(
            width=35, justify="center", padx=2, pady=2, bg="#c8a6cb",
            relief="ridge", bd=2)

        label_quantity_desired.grid(
            row=0, column=0, padx=(15, 15), pady=(15, 15))

        show_quantity_desired = tk.Label(frame_quantity_desired, text=0)

        show_quantity_desired.config(
            width=15, justify="center", padx=2, pady=2, bg="white",
            relief="ridge", bd=2)

        show_quantity_desired.grid(row=1, column=0, padx=(0, 0), pady=(0, 15))

        entry_value_quantity_desired = tk.IntVar()

        entry_quantity_desired = tk.Entry(
            frame_quantity_desired, textvariable=entry_value_quantity_desired)

        entry_quantity_desired.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2)

        entry_quantity_desired.grid(row=0, column=1, padx=(0, 15), pady=(0, 0))

        self.entry_quantity_desired = entry_quantity_desired.get()

        calcul_quantity_desired = pkg_functions_utils.FunctionsCommandButton()
        calcul_quantity_desired.calcul_by_quantity_desired(frame_quantity_desired)

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

        show_aroma = tk.Label(frame_aroma, text=0)

        show_aroma.config(
            width=15, justify="center", padx=2, pady=2, bg="white",
            relief="ridge", bd=2)

        show_aroma.grid(row=1, column=0, padx=(0, 0), pady=(0, 15))

        entry_value_aroma = tk.IntVar()

        entry_aroma = tk.Entry(frame_aroma, textvariable=entry_value_aroma)

        entry_aroma.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2)

        entry_aroma.grid(row=0, column=1, padx=(0, 15), pady=(0, 0))

        button_aroma = tk.Button(frame_aroma, text="Valid")
        button_aroma.place(x=334, y=50)

        self.entry_aroma = entry_aroma.get()

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

        show_base = tk.Label(frame_base, text=0)
        show_base.config(
            width=15, justify="center", padx=2, pady=2, bg="white",
            relief="ridge", bd=2)

        show_base.grid(row=1, column=0, padx=(0, 0), pady=(0, 15))

        entry_value_base = tk.IntVar()
        entry_base = tk.Entry(frame_base, textvariable=entry_value_base)
        entry_base.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2)

        entry_base.grid(row=0, column=1, padx=(0, 15), pady=(0, 0))

        button_base = tk.Button(frame_base, text="Valid")
        button_base.place(x=334, y=50)

        self.entry_base = entry_base.get()
