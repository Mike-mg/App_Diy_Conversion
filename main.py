# Main window

import sys
import tkinter as tk
from PIL import Image, ImageTk
import pkg_widgets

bg = "#f28de2"

# Init window Tkinter ---------------------------------------------------------

window = tk.Tk()
if sys.platform.startswith("linux"):
    icon = tk.PhotoImage(file='images/icone.gif')
    window.tk.call('wm', 'iconphoto', window._w, icon)

elif sys.platform.startswith("win32"):
    window.iconbitmap("images/icone.ico")

window.title("Diy - Vap")
window.geometry("550x650")
window.resizable(0, 0)

# Image background ------------------------------------------------------------

image = ImageTk.PhotoImage(Image.open("/home/mike/Images/background.jpeg"))
image_label = tk.Label(image=image)
image_label.place(x=0, y=0)

# Frame and widgets selects dosage --------------------------------------------

percent_dosage = pkg_widgets.FramesWidgets(window)
percent_dosage.frame_dosage((50, 0), (50, 0))


# Quantity desired ------------------------------------------------------------

quantity_desired = pkg_widgets.FramesWidgets(window)
quantity_desired.frame_quantity((50, 0), (25, 0))


# Quantity of aroma -----------------------------------------------------------

quantity_aroma = pkg_widgets.FramesWidgets(window)
quantity_aroma.frame_aroma((50, 0), (25, 0))

# Quantity of base ------------------------------------------------------------

quantity_base = pkg_widgets.FramesWidgets(window)
quantity_base.frame_base((50, 0), (25, 0))

# End Main window =============================================================

window.mainloop()
