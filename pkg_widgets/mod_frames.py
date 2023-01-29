# Widget dosage

import tkinter as tk
import pkg_utils_class_tkinter


class FramesWidgets:
    # Class frame of program

    def __init__(self, window) -> None:
        self.window = window
        self.bg = "#f28de2"

    def frame_dosage(self, padx=(0, 0), pady=(0, 0)) -> None:
        # Show frame percent dosage

        frame_selected_dosage = tk.Frame(
            self.window, borderwidth=2, relief="raised", bg=self.bg, border=3
        )

        frame_selected_dosage.grid(row=0, column=0, padx=padx, pady=pady)

        selected_dosage = pkg_utils_class_tkinter.LabelText(
            frame_selected_dosage, "Selected dosage"
        )

        selected_dosage.label_texte.config(padx=2, pady=2, bg=self.bg)

        selected_dosage.label_grid(row=0, column=0, padx=(0, 0), pady=(0, 0))

        percent_aroma = tk.Scale(
            frame_selected_dosage,
            digits=2,
            length=375,
            from_=0,
            to=20,
            orient="horizontal",
            bg=self.bg,
            troughcolor="white",
            font=("Arial", 14),
            fg="white",
            variable=0,
        )

        percent_aroma.grid(row=1, column=0)

    def frame_quantity(self, padx=(0, 0), pady=(0, 0)) -> None:
        # show frame quantity desired

        frame_quantity_desired = tk.Frame(
            self.window, borderwidth=3, relief="raised", bg=self.bg
        )

        frame_quantity_desired.grid(row=1, column=0, padx=padx, pady=pady)

        label_quantity_desired = pkg_utils_class_tkinter.LabelText(
            frame_quantity_desired, "Quantity total"
        )

        label_quantity_desired.label_texte.config(
            width=35, justify="center", padx=2, pady=2, bg="#c8a6cb",
            relief="ridge", bd=2,
        )

        label_quantity_desired.label_grid(
            row=0, column=0, padx=(15, 15), pady=(15, 15))

        show_quantity_desired = pkg_utils_class_tkinter.LabelText(
            frame_quantity_desired, 0
        )

        show_quantity_desired.label_texte.config(
            width=15, justify="center", padx=2, pady=2, bg="white",
            relief="ridge", bd=2
        )

        show_quantity_desired.label_grid(
            row=1, column=0, padx=(0, 0), pady=(0, 15))

        entry_quantity_desired = pkg_utils_class_tkinter.ValueEntry(
            frame_quantity_desired, 0
        )

        entry_quantity_desired.entry_textvariable.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2
        )

        entry_quantity_desired.enrty_grid(
            row=0, column=1, padx=(0, 15), pady=(0, 0))

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

        frame_aroma.grid(row=2, column=0, padx=(50, 0), pady=(25, 0))

        label_aroma = pkg_utils_class_tkinter.LabelText(
            frame_aroma, "Quantity of aroma"
        )

        label_aroma.label_texte.config(
            width=35, justify="center", padx=2, pady=2, bg="#c8a6cb",
            relief="ridge", bd=2,
        )

        label_aroma.label_grid(row=0, column=0, padx=(15, 15), pady=(15, 10))

        show_label_aroma = pkg_utils_class_tkinter.LabelText(frame_aroma, 0)

        show_label_aroma.label_texte.config(
            width=15, justify="center", padx=2, pady=2, bg="white",
            relief="ridge", bd=2
        )

        show_label_aroma.label_grid(row=1, column=0, padx=(0, 0), pady=(0, 15))

        entry_aroma = pkg_utils_class_tkinter.ValueEntry(frame_aroma, 0)
        entry_aroma.entry_textvariable.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2
        )

        entry_aroma.enrty_grid(row=0, column=1, padx=(0, 15), pady=(0, 0))

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

        frame_base.grid(row=3, column=0, padx=(50, 0), pady=(25, 0))

        base = pkg_utils_class_tkinter.LabelText(
            frame_base, "Quantity of base")

        base.label_texte.config(width=35, justify="center", padx=2, pady=2,
                                bg="#c8a6cb", relief="ridge", bd=2
                                )

        base.label_grid(row=0, column=0, padx=(15, 15), pady=(15, 10))

        show_label_base = pkg_utils_class_tkinter.LabelText(frame_base, 0)
        show_label_base.label_texte.config(
            width=15, justify="center", padx=2, pady=2, bg="white",
            relief="ridge", bd=2
        )

        show_label_base.label_grid(row=1, column=0, padx=(0, 0), pady=(0, 15))

        entry_base = pkg_utils_class_tkinter.ValueEntry(frame_base, 0)
        entry_base.entry_textvariable.config(
            width=10, justify="center", bg="white", relief="ridge", bd=2
        )

        entry_base.enrty_grid(row=0, column=1, padx=(0, 15), pady=(0, 0))

        # command_button_results_calculs = results_calculs()

        button_quantity = tk.Button(frame_base, text="Valid")
        # command=command_button_results_calculs.calcul_by_quantity_desired()
        button_quantity.place(x=334, y=50)
