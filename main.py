# Main window

import sys
import tkinter as tk
from PIL import Image, ImageTk
import pkg_utils_class_tkinter

dosage = {"diy": 0, "base": 0, "arome": 0, "qty_totale": 0}
bg = "#d5d7a0"

# Init window Tkinter ---------------------------------------------------------

window = tk.Tk()
if sys.platform.startswith("linux"):
    icon = tk.PhotoImage(file='images/icone.gif')
    window.tk.call('wm', 'iconphoto', window._w, icon)

elif sys.platform.startswith("win32"):
    window.iconbitmap("images.icone.ico")

window.title("Diy - Vap")
window.geometry("516x601")
window.resizable(0, 0)

# Image background ------------------------------------------------------------

image = ImageTk.PhotoImage(Image.open("images/background.jpg"))
image_label = tk.Label(image=image)
image_label.place(x=0, y=0)

# Frame selects dosage --------------------------------------------------------

frame_selected_dosage = tk.Frame(
    window, borderwidth=1, relief="raised", padx=10, pady=10, bg="#91149c",
    border=2)

frame_selected_dosage.grid(row=0, column=0, padx=(25, 0), pady=(25, 25))

selected_dosage = pkg_utils_class_tkinter.LabelText(
    frame_selected_dosage, "Selected dosage"
)

selected_dosage.label_texte.config(width=35, padx=2, pady=2, bg="#c8a6cb")

selected_dosage.label_grid(row=0, column=0, padx=(0, 0), pady=(0, 10))

percent_aroma = tk.Scale(
    frame_selected_dosage,
    digits=2,
    length=375,
    from_=0,
    to=20,
    orient="horizontal",
    bg="#91149c",
    troughcolor="white",
    font=("Arial", 14),
    fg="white",
    variable=0,
)

percent_aroma.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))

# Quantity desired ------------------------------------------------------------

frame_quantity_desired_main = tk.Frame(
    window, borderwidth=1, relief="raised", padx=10, pady=10, bg="#91149c",
    border=2)

frame_quantity_desired_main.grid(row=1, column=0, padx=(25, 0), pady=(0, 25))

frame_annex_frame_quantity_desired_main = tk.Frame(
    frame_quantity_desired_main,
    borderwidth=1,
    relief="raised",
    padx=0,
    pady=0,
    bg="#91149c",
    border=2,
)

frame_annex_frame_quantity_desired_main.grid(row=0, column=0, padx=(0, 25),
                                             pady=(0, 0))

label_quantity_desired = pkg_utils_class_tkinter.LabelText(
    frame_quantity_desired_main, "Quantity total"
)

label_quantity_desired.label_texte.config(
    width=35, justify="center", padx=2, pady=2, bg="#c8a6cb"
)

label_quantity_desired.label_grid(row=0, column=0, padx=(0, 0), pady=(0, 10))

show_quantity_desired = pkg_utils_class_tkinter.LabelText(
    frame_quantity_desired_main, 0
)

show_quantity_desired.label_texte.config(
    width=35, justify="center", padx=2, pady=2, bg="white"
)

show_quantity_desired.label_grid(row=1, column=0, padx=(0, 0), pady=(0, 0))

entry_quantity_desired = pkg_utils_class_tkinter.ValueEntry(
    frame_quantity_desired_main, 0
)
entry_quantity_desired.entry_textvariable.config(width=15, justify="center")
entry_quantity_desired.enrty_grid(row=0, column=1, rowspan=2, padx=(25, 0),
                                  pady=(0, 0))

# Quantity of aroma -----------------------------------------------------------

frame_aroma = tk.Frame(
    window, borderwidth=1, relief="raised", padx=10, pady=10, bg="#91149c"
)
frame_aroma.grid(row=2, column=0, padx=(25, 0), pady=(0, 25))

label_aroma = pkg_utils_class_tkinter.LabelText(frame_aroma,
                                                "Quantity of aroma")

label_aroma.label_texte.config(width=35, justify="center", padx=2, pady=2,
                               bg="#c8a6cb")

label_aroma.label_grid(row=0, column=0, padx=(0, 0), pady=(0, 10))

show_label_aroma = pkg_utils_class_tkinter.LabelText(frame_aroma, 0)

show_label_aroma.label_texte.config(
    width=35, justify="center", padx=2, pady=2, bg="white"
)

show_label_aroma.label_grid(row=1, column=0, padx=(0, 0), pady=(0, 0))

entry_aroma = pkg_utils_class_tkinter.ValueEntry(frame_aroma, 0)
entry_aroma.entry_textvariable.config(width=15, justify="center")
entry_aroma.enrty_grid(row=0, column=1, rowspan=2, padx=(25, 0), pady=(0, 0))

# Quantity of base ------------------------------------------------------------

frame_base = tk.Frame(
    window, borderwidth=1, relief="raised", padx=10, pady=10, bg="#91149c"
)
frame_base.grid(row=3, column=0, padx=(25, 0), pady=(0, 0))

base = pkg_utils_class_tkinter.LabelText(frame_base, "Quantity of base")
base.label_texte.config(width=35, justify="center", padx=2, pady=2,
                        bg="#c8a6cb")

base.label_grid(row=0, column=0, padx=(0, 0), pady=(0, 10))

show_label_base = pkg_utils_class_tkinter.LabelText(frame_base, 0)
show_label_base.label_texte.config(
    width=35, justify="center", padx=2, pady=2, bg="white"
)

show_label_base.label_grid(row=1, column=0, padx=(0, 0), pady=(0, 0))

entry_base = pkg_utils_class_tkinter.ValueEntry(frame_base, 0)
entry_base.entry_textvariable.config(width=15, justify="center")
entry_base.enrty_grid(row=0, column=1, rowspan=2, padx=(25, 0), pady=(0, 0))


# Button function -------------------------------------------------------------

def calcul():

    percent_dosage = {"aroma": percent_aroma.get()}, {"base": 100}

    if entry_aroma.int_entry.get() > 0:

        base = entry_aroma.int_entry.get(
        ) * percent_dosage[1]["base"] // percent_dosage[0]["aroma"] # noqa
        quantite_total = base + entry_aroma.int_entry.get()

        show_quantity_desired.label_texte["text"] = str(quantite_total)
        show_label_aroma.label_texte["text"] = str(entry_aroma.int_entry.get())
        show_label_base.label_texte["text"] = str(base)

        entry_aroma.int_entry.set(0)

    elif entry_base.int_entry.get() > 0:

        aroma = entry_base.int_entry.get() * percent_aroma.get(
        ) // percent_dosage[1]["base"]
        quantite_total = entry_base.int_entry.get() + aroma

        show_quantity_desired.label_texte["text"] = str(quantite_total)
        show_label_aroma.label_texte["text"] = str(aroma)
        show_label_base.label_texte["text"] = str(entry_base.int_entry.get())

        entry_base.int_entry.set(0)


button = tk.Button(
    window, width=20, text="Valide", font=("arial, 10"), borderwidth=3,
    command=calcul)

button.grid(row=4, column=0, padx=(0, 0), pady=(50, 0))

# End Main window =============================================================

window.mainloop()
