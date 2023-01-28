# Function program

from tkinter import messagebox as messagebox

percent_dosage = {"aroma": main.percent_aroma.get()}, {"base": 100}


class results_calculs:

    def __init__(self) -> None:
        pass

    def reset_variable(self):
        # Reset variable type entry and percent_arome if error

        main.entry_aroma.int_entry.set(0)
        main.entry_base.int_entry.set(0)
        main.entry_quantity_desired.int_entry.set(0)
        main.percent_aroma.set(0)

    def calcul_by_quantity_desired(self):

        try:

            if main.entry_quantity_desired.int_entry.get() > 0:

                base = main.entry_quantity_desired.int_entry.get(
                ) * percent_dosage[1]["base"] / (
                    main.percent_aroma.get() + percent_dosage[1]["base"])

                base = round(base, 2)

                aroma = base * main.percent_aroma.get(
                ) / percent_dosage[1]["base"]

                aroma = round(aroma, 1)

                main.show_quantity_desired.label_texte["text"] = str(
                    main.entry_quantity_desired.int_entry.get())
                main.show_label_aroma.label_texte["text"] = str(aroma)
                main.show_label_base.label_texte["text"] = str(base)

                main.entry_quantity_desired.int_entry.set(0)

        except Exception:
            messagebox.showerror(title="Erreur de saisie",
            message="Erreur de saisie\nTous les champs non utilisés doivent être à 0.\nLes champs vont être réinitialisés") # noqa

            self.reset_variable()

    # def calcul_by_aroma(self):

    #     try:
    #         if main.entry_aroma.int_entry.get() > 0:

    #             base = main.entry_aroma.int_entry.get(
    #             ) * percent_dosage[1]["base"] / percent_dosage[0]["aroma"]

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
    #             ) * main.percent_aroma.get() / percent_dosage[1]["base"]

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
