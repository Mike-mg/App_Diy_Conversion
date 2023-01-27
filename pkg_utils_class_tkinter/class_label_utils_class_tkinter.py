# Define the useful classes of Tkinter

import tkinter as tk


class LabelTextVariable:
    # Class for the Label Tkinter

    def __init__(self, window, int_label):
        self.int_label = tk.DoubleVar()
        self.int_label.set(int_label)
        self.label_textevariable = tk.Label(window,
                                            textvariable=self.int_label)

    def label_grid(
        self, row, column, rowspan=1, columnspan=1, padx=(0, 0), pady=(0, 0)
    ) -> None:
        # Place the label in the window tkinter

        self.label_textevariable.grid(
            row=row,
            column=column,
            rowspan=rowspan,
            columnspan=columnspan,
            padx=padx,
            pady=pady,
        )


class LabelText:
    # Class for the Label Tkinter

    def __init__(self, window, text):
        self.label_texte = tk.Label(window, text=text)

    def label_grid(
        self, row, column, rowspan=1, columnspan=1, padx=(0, 0), pady=(0, 0)
    ) -> None:
        # Place the label in the window tkinter

        self.label_texte.grid(
            row=row,
            column=column,
            rowspan=rowspan,
            columnspan=columnspan,
            padx=padx,
            pady=pady,
        )


class ValueEntry:
    # Class for the entry Tkinter

    def __init__(self, window, int_label):
        self.int_entry = tk.DoubleVar()
        self.int_entry.set(int_label)
        self.entry_textvariable = tk.Entry(window, textvariable=self.int_entry)

    def enrty_grid(
        self, row, column, rowspan=1, columnspan=1, padx=(0, 0), pady=(0, 0)
    ):
        # Place the label in the window tkinter

        self.entry_textvariable.grid(
            row=row,
            column=column,
            rowspan=rowspan,
            columnspan=columnspan,
            padx=padx,
            pady=pady,
        )
