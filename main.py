# Main window

from pkg_window_tkinter import MainWindowApp
from PIL import ImageTk, Image
import tkinter as tk

# # Init window Tkinter ---------------------------------------------------------

window = MainWindowApp()
window.verify_sysytem_for_icon()
window.config_windows_tk()
window.image_background(window.window)
window.window.mainloop()

# Frame and widgets selects dosage --------------------------------------------

# percent_dosage = pkg_widgets.FramesWidgets(window)
# percent_dosage.frame_dosage((50, 0), (50, 0))


# Quantity desired ------------------------------------------------------------

# quantity_desired = pkg_widgets.FramesWidgets(window)
# quantity_desired.frame_quantity((50, 0), (25, 0))


# Quantity of aroma -----------------------------------------------------------

# quantity_aroma = pkg_widgets.FramesWidgets(window)
# quantity_aroma.frame_aroma((50, 0), (25, 0))

# Quantity of base ------------------------------------------------------------

# quantity_base = pkg_widgets.FramesWidgets(window)
# quantity_base.frame_base((50, 0), (25, 0))

# # End Main window =============================================================

# window.mainloop()


