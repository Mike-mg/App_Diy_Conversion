# Main window

import sys
import tkinter as tk
from tkinter import messagebox as messagebox
from PIL import Image, ImageTk
import pkg_utils_class_tkinter

bg = "#f28de2"

# Init window Tkinter ---------------------------------------------------------

window = tk.Tk()
if sys.platform.startswith("linux"):
    icon = tk.PhotoImage(file='images/icone.gif')
    window.tk.call('wm', 'iconphoto', window._w, icon)

elif sys.platform.startswith("win32"):
    window.iconbitmap("images.icone.ico")

window.title("Diy - Vap")
window.geometry("525x650")
window.resizable(0, 0)

# Image background ------------------------------------------------------------

image = ImageTk.PhotoImage(Image.open("images/background.jpg"))
image_label = tk.Label(image=image)
image_label.place(x=0, y=0)

# Frame selects dosage --------------------------------------------------------

frame_selected_dosage = tk.Frame(
    window, borderwidth=2, relief="raised", bg=bg,
    border=3)

frame_selected_dosage.grid(row=0, column=0, padx=(50, 0), pady=(50, 0))

selected_dosage = pkg_utils_class_tkinter.LabelText(
    frame_selected_dosage, "Selected dosage")

selected_dosage.label_texte.config(padx=2, pady=2, bg=bg)

selected_dosage.label_grid(row=0, column=0, padx=(0, 0), pady=(0, 0))

percent_aroma = tk.Scale(
    frame_selected_dosage,
    digits=2,
    length=375,
    from_=0,
    to=20,
    orient="horizontal",
    bg=bg,
    troughcolor="white",
    font=("Arial", 14),
    fg="white",
    variable=0,
)

percent_aroma.grid(row=1, column=0)

# Quantity desired ------------------------------------------------------------

frame_quantity_desired_main = tk.Frame(
    window, borderwidth=3, relief="raised", bg=bg)

frame_quantity_desired_main.grid(row=1, column=0, padx=(50, 0), pady=(25, 0))

label_quantity_desired = pkg_utils_class_tkinter.LabelText(
    frame_quantity_desired_main, "Quantity total")

label_quantity_desired.label_texte.config(width=35, justify="center", padx=2,
                                          pady=2, bg="#c8a6cb",
                                          relief="ridge", bd=2)

label_quantity_desired.label_grid(
    row=0, column=0, padx=(15, 15), pady=(15, 10))

show_quantity_desired = pkg_utils_class_tkinter.LabelText(
    frame_quantity_desired_main, 0)

show_quantity_desired.label_texte.config(width=15, justify="center", padx=2,
                                         pady=2, bg="white", relief="ridge",
                                         bd=2)

show_quantity_desired.label_grid(row=1, column=0, padx=(0, 0), pady=(0, 15))

entry_quantity_desired = pkg_utils_class_tkinter.ValueEntry(
    frame_quantity_desired_main, 0)

entry_quantity_desired.entry_textvariable.config(width=10, justify="center",
                                                 bg="white", relief="ridge",
                                                 bd=2)

entry_quantity_desired.enrty_grid(row=0, column=1, rowspan=2, padx=(0, 15),
                                  pady=(0, 0))

# Quantity of aroma -----------------------------------------------------------

frame_aroma = tk.Frame(window, borderwidth=3, relief="raised",
                       padx=0, pady=0, bg=bg)

frame_aroma.grid(row=2, column=0, padx=(50, 0), pady=(25, 0))

label_aroma = pkg_utils_class_tkinter.LabelText(frame_aroma,
                                                "Quantity of aroma")

label_aroma.label_texte.config(width=35, justify="center", padx=2,
                               pady=2, bg="#c8a6cb",
                               relief="ridge", bd=2)

label_aroma.label_grid(row=0, column=0, padx=(15, 15), pady=(15, 10))

show_label_aroma = pkg_utils_class_tkinter.LabelText(frame_aroma, 0)

show_label_aroma.label_texte.config(width=15, justify="center", padx=2, pady=2,
                                    bg="white", relief="ridge", bd=2)

show_label_aroma.label_grid(row=1, column=0, padx=(0, 0), pady=(0, 15))

entry_aroma = pkg_utils_class_tkinter.ValueEntry(frame_aroma, 0)
entry_aroma.entry_textvariable.config(width=10, justify="center", bg="white",
                                      relief="ridge", bd=2)

entry_aroma.enrty_grid(row=0, column=1, rowspan=2, padx=(0, 15), pady=(0, 0))

# Quantity of base ------------------------------------------------------------

frame_base = tk.Frame(window, borderwidth=3, relief="raised",
                      padx=0, pady=0, bg=bg)

frame_base.grid(row=3, column=0, padx=(50, 0), pady=(25, 0))

base = pkg_utils_class_tkinter.LabelText(frame_base, "Quantity of base")
base.label_texte.config(width=35, justify="center", padx=2,
                        pady=2, bg="#c8a6cb",
                        relief="ridge", bd=2)

base.label_grid(row=0, column=0, padx=(15, 15), pady=(15, 10))

show_label_base = pkg_utils_class_tkinter.LabelText(frame_base, 0)
show_label_base.label_texte.config(width=15, justify="center", padx=2, pady=2,
                                   bg="white", relief="ridge", bd=2)

show_label_base.label_grid(row=1, column=0, padx=(0, 0), pady=(0, 15))

entry_base = pkg_utils_class_tkinter.ValueEntry(frame_base, 0)
entry_base.entry_textvariable.config(width=10, justify="center", bg="white",
                                     relief="ridge", bd=2)

entry_base.enrty_grid(row=0, column=1, rowspan=2, padx=(0, 15), pady=(0, 0))


# Button function -------------------------------------------------------------

def calcul():

    try:
        percent_dosage = {"aroma": percent_aroma.get()}, {"base": 100}

        if entry_aroma.int_entry.get() > 0:

            base = entry_aroma.int_entry.get(
            ) * percent_dosage[1]["base"] / percent_dosage[0]["aroma"] # noqa

            base = round(base, 2)

            quantite_total = base + entry_aroma.int_entry.get()

            show_quantity_desired.label_texte["text"] = str(quantite_total)
            show_label_aroma.label_texte["text"] = str(
                entry_aroma.int_entry.get())
            show_label_base.label_texte["text"] = str(base)

            entry_aroma.int_entry.set(0)

        elif entry_base.int_entry.get() > 0:

            aroma = entry_base.int_entry.get(
            ) * percent_aroma.get() / percent_dosage[1]["base"]

            aroma = round(aroma, 2)

            quantite_total = entry_base.int_entry.get() + aroma

            show_quantity_desired.label_texte["text"] = str(quantite_total)
            show_label_aroma.label_texte["text"] = str(aroma)
            show_label_base.label_texte["text"] = str(
                entry_base.int_entry.get())

            entry_base.int_entry.set(0)

        elif entry_quantity_desired.int_entry.get() > 0:

            base = entry_quantity_desired.int_entry.get(
            ) * percent_dosage[1]["base"] / (
                percent_aroma.get() + percent_dosage[1]["base"])

            base = round(base, 2)

            aroma = base * percent_aroma.get() / percent_dosage[1]["base"]

            aroma = round(aroma, 2)

            show_quantity_desired.label_texte["text"] = str(
                entry_quantity_desired.int_entry.get())
            show_label_aroma.label_texte["text"] = str(aroma)
            show_label_base.label_texte["text"] = str(base)

            entry_quantity_desired.int_entry.set(0)

    except Exception:
        messagebox.showerror(
            title="Erreur de saisie",
            message="Erreur de saisie\nTous les champs non utilisés doivent être à 0.\nLes champs vont être réinitialisés") # noqa

        entry_aroma.int_entry.set(0)
        entry_base.int_entry.set(0)
        entry_quantity_desired.int_entry.set(0)
        percent_aroma.set(0)


button = tk.Button(
    window, width=20, text="Valide", font=("arial, 10"), borderwidth=3,
    command=calcul)

button.grid(row=4, column=0, padx=(50, 0), pady=(50, 0))

# End Main window =============================================================

window.mainloop()
