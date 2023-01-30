# Function calcul of program

import tkinter as tk
from tkinter import messagebox as messagebox
import pkg_widgets


class FunctionsCommandButton:
    # Class for the command button

    def __init__(self) -> None:
        self.widgets = pkg_widgets.FramesWidgets()
        self.dict_percent_aroma = {
            "aroma": self.widgets.selected_percent_dosage}, {"base": 100}

        self.selected_percent_aroma = self.widgets.selected_percent_dosage

        self.entry_quantity_desired = self.widgets.entry_quantity_desired
        self.entry_aroma = self.widgets.entry_aroma
        self.entry_base = self.widgets.entry_base

        self.show_quantity_desired = self.widgets.show_quantity_desired
        self.show_aroma = self.widgets.show_aroma
        self.show_base = self.widgets.show_base

# Calcul with quantity desired ------------------------------------------------

    def button_command_quantity_desired(self, window):

        button_quantity = tk.Button(
            window, text="Valid", command=self.calcul_by_quantity_desired)

        button_quantity.place(x=334, y=50)

    def calcul_by_quantity_desired(self, window):

        self.button_command_quantity_desired(window)

        try:

            if self.entry_quantity_desired > 0:

                base = self.entry_quantity_desired * self.dict_percent_aroma[
                    1]["base"] / (
                        self.selected_percent_aroma + self.dict_percent_aroma[
                            1]["base"])

                base = round(base, 1)

                aroma = base \
                    * self.selected_percent_aroma \
                    / self.dict_percent_aroma[1]["base"]

                aroma = round(aroma, 1)

                self.show_quantity_desired["text"] = str(self.entry_quantity_desired)
                self.show_aroma["text"] = str(self.entry_aroma)
                self.show_base["text"] = str(self.entry_base)

        except Exception:
            messagebox.showerror(
                title="Erreur de saisie",
                message="Erreur de saisie\nTous les champs non utilisés \
                    doivent être à 0.\nLes champs vont être réinitialisés") # noqa

    # def calcul_by_aroma(self):

    #     try:
    #         if main.entry_aroma.int_entry.get() > 0:

    #             base = main.entry_aroma.int_entry.get(
    #             ) * self.functions_calculs.self.functions_calculs.self.functions_calculs.self.functions_calculs.self.functions_calculs.percent_dosage[1]["base"] / self.functions_calculs.self.functions_calculs.self.functions_calculs.self.functions_calculs.self.functions_calculs.percent_dosage[0]["aroma"]

    #             base = round(base, 2)

    #             quantite_total = base + main.entry_aroma.int_entry.get()

    #             main.show_quantity_desired.label_texte["text"] = str(
    #                 quantite_total)

    #             main.show_label_aroma.label_texte["text"] = str(
    #                 main.entry_aroma.int_entry.get())

    #             main.show_label_base.label_texte["text"] = str(base)

    #             main.entry_aroma.int_entry.set(0)

    #     except Exception:
    #         messagebox.showerror(title="Erreur de saisie",
    #         message="Erreur de saisie\nTous les champs non utilisés doivent être à 0.\nLes champs vont être réinitialisés") # noqa

    #         self.reset_variable()

    # def calcul_by_base(self):

    #     try:

    #         if main.entry_base.int_entry.get() > 0:

    #             aroma = main.entry_base.int_entry.get(
    #             ) * self.functions_calculs.percent_dosage.get() / self.functions_calculs.self.functions_calculs.self.functions_calculs.self.functions_calculs.self.functions_calculs.percent_dosage[1]["base"]

    #             aroma = round(aroma, 2)

    #             quantite_total = main.entry_base.int_entry.get() + aroma

    #             main.show_quantity_desired.label_texte["text"] = str(
    #                 quantite_total)

    #             main.show_label_aroma.label_texte["text"] = str(aroma)
    #             main.show_label_base.label_texte["text"] = str(
    #                 main.entry_base.int_entry.get())

    #             main.entry_base.int_entry.set(0)

    #     except Exception:
    #         messagebox.showerror(
    #             title="Erreur de saisie",
    #             message="Erreur de saisie\nTous les champs non utilisés doivent être à 0.\nLes champs vont être réinitialisés") # noqa

    #         self.reset_variable()
