# Function program

from tkinter import messagebox as messagebox
import main


def calcul_by_quantity_desired():

    percent_dosage = {"aroma": main.percent_aroma.get()}, {"base": 100}

    try:

        if main.entry_quantity_desired.int_entry.get() > 0:

            base = main.entry_quantity_desired.int_entry.get(
            ) * percent_dosage[1]["base"] / (
                main.percent_aroma.get() + percent_dosage[1]["base"])

            base = round(base, 2)

            aroma = base * main.percent_aroma.get() / percent_dosage[1]["base"]

            aroma = round(aroma, 1)

            main.show_quantity_desired.label_texte["text"] = str(
                main.entry_quantity_desired.int_entry.get())
            main.show_label_aroma.label_texte["text"] = str(aroma)
            main.show_label_base.label_texte["text"] = str(base)

            main.entry_quantity_desired.int_entry.set(0)

    except Exception:
        messagebox.showerror(title="Erreur de saisie",
        message="Erreur de saisie\nTous les champs non utilisés doivent être à 0.\nLes champs vont être réinitialisés") # noqa
