# Widgets frames

import tkinter as tk
# import pkg_utils_class_tkinter


class FramesWidgets:
    # Class frames of program

    def __init__(self, window) -> None:
        self.window = window
        self.bg = "#f28de2"

    def frame_dosage(self) -> None:
        # Show frame percent dosage

        frame_selected_dosage = tk.Frame(
            self.window, borderwidth=2, relief="raised", bg=self.bg, border=3
        )

        frame_selected_dosage.grid(row=0, column=0, padx=(50, 0), pady=(50, 25))

        label_selected_dosage = tk.Label(
            frame_selected_dosage, text="Selected dosage")
        
        label_selected_dosage.grid(row=0, column=0, padx=(0, 0), pady=(0, 0))

        percent_aroma = tk.Scale(frame_selected_dosage, digits=2, length=375,
                                 from_=0, to=20, orient="horizontal",
                                 bg=self.bg, troughcolor="white", 
                                 font=("Arial", 14), fg="white", variable=0)

        percent_aroma.grid(row=1, column=0)

    def frame_quantity(self) -> None:
        # show frame quantity desired

        frame_quantity_desired = tk.Frame(
            self.window, borderwidth=3, relief="raised", bg=self.bg
        )

        frame_quantity_desired.grid(row=1, column=0, padx=(50, 0), pady=(0, 25))

        label_quantity_desired = tk.Label(
            frame_quantity_desired, text="Quantity total")
        
        label_quantity_desired.grid(row=0, column=0, padx=(0, 0), pady=(0, 0))

        label_quantity_desired.config(
                width=35, justify="center", padx=2, pady=2, bg="#c8a6cb",
                relief="ridge", bd=2,
            )

        label_quantity_desired.grid(
            row=0, column=0, padx=(15, 15), pady=(15, 15))

        show_quantity_desired = tk.Label(frame_quantity_desired, text=0)

        show_quantity_desired.config(width=15, justify="center", padx=2,
                                     pady=2, bg="white", relief="ridge", bd=2)

        show_quantity_desired.grid(
            row=1, column=0, padx=(0, 0), pady=(0, 15))

        entry_quantity_desired = tk.Entry(frame_quantity_desired, text=0)

        entry_quantity_desired.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2)

        entry_quantity_desired.grid(row=0, column=1, padx=(0, 15), pady=(0, 0))

        # command_button_results_calculs = results_calculs()

        button_quantity = tk.Button(frame_quantity_desired, text="Valid",)
        # command=command_button_results_calculs.calcul_by_quantity_desired()
        button_quantity.place(x=334, y=50)

    def frame_aroma(self, padx=(0, 0), pady=(0, 0)) -> None:
        # show frame quantity aroma

        frame_aroma = tk.Frame(
            self.window, borderwidth=3, relief="raised",
            padx=0, pady=0, bg=self.bg
        )

        frame_aroma.grid(row=2, column=0, padx=(50, 0), pady=(0, 25))

        label_aroma = tk.Label(frame_aroma, text="Quantity of aroma")

        label_aroma.config(
            width=35, justify="center", padx=2, pady=2, bg="#c8a6cb",
            relief="ridge", bd=2,
        )

        label_aroma.grid(row=0, column=0, padx=(15, 15), pady=(15, 10))

        show_label_aroma = tk.Label(frame_aroma, text=0)

        show_label_aroma.config(
            width=15, justify="center", padx=2, pady=2, bg="white",
            relief="ridge", bd=2
        )

        show_label_aroma.grid(row=1, column=0, padx=(0, 0), pady=(0, 15))

        entry_aroma = tk.Entry(frame_aroma, text=0)
        entry_aroma.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2)

        entry_aroma.grid(row=0, column=1, padx=(0, 15), pady=(0, 0))

        # command_button_results_calculs = results_calculs()

        button_quantity = tk.Button(frame_aroma, text="Valid")
        # command=command_button_results_calculs.calcul_by_quantity_desired()
        button_quantity.place(x=334, y=50)

    def frame_base(self, padx=(0, 0), pady=(0, 0)) -> None:
        # show frame quantity base

        frame_base = tk.Frame(
            self.window, borderwidth=3, relief="raised", padx=0, pady=0,
            bg=self.bg
        )

        frame_base.grid(row=3, column=0, padx=(50, 0), pady=(0, 0))

        base = tk.Label(frame_base, text="Quantity of base")

        base.config(
            width=35, justify="center", padx=2, pady=2, bg="#c8a6cb",
            relief="ridge", bd=2)

        base.grid(row=0, column=0, padx=(15, 15), pady=(15, 10))

        show_label_base = tk.Label(frame_base, text=0)
        show_label_base.config(
            width=15, justify="center", padx=2, pady=2, bg="white",
            relief="ridge", bd=2
        )

        show_label_base.grid(row=1, column=0, padx=(0, 0), pady=(0, 15))

        entry_base = tk.Entry(frame_base, text=0)
        entry_base.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2
        )

        entry_base.grid(row=0, column=1, padx=(0, 15), pady=(0, 0))

        # command_button_results_calculs = results_calculs()

        button_quantity = tk.Button(frame_base, text="Valid")
        # command=command_button_results_calculs.calcul_by_quantity_desired()
        button_quantity.place(x=334, y=50)
