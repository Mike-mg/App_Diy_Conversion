# # Main window of program

import tkinter as tk
import sys
from PIL import Image, ImageTk
import pkg_widgets


class MainWindowApp:
    # Main window

    def __init__(self):

        self.window = tk.Tk()
        self.bg = "#f28de2"
        self.background = ImageTk.PhotoImage(
            Image.open("images/background.png"))

        self.widgets = pkg_widgets.FramesWidgets()

    def verify_sysytem_for_icon(self) -> None:
        # Displays the icon according to the system

        if sys.platform.startswith("linux"):
            icon = tk.PhotoImage(file="images/icone.gif")
            self.window.call("wm", "iconphoto", self.window._w, icon)

        elif sys.platform.startswith("win32"):
            self.window.iconbitmap("images/icone.ico")

    def config_window(self) -> None:
        # Configure the main window

        self.window.title("Diy - Vap")
        self.window.geometry("525x575")
        self.window.resizable(0, 0)

    def image_background(self):
        # Configure background image

        tk.Label(self.window, image=self.background).place(x=0, y=0)

    def frame_percent_dosage_aroma(self):
        # Show frame select dosage percent

        self.widgets.frame_percent_dosage_aroma(self.window)

    def frame_quantity(self):
        # Show frame quantity

        self.widgets.frame_quantity(self.window)

    def frame_aroma(self):
        # Show frame aroma

        self.widgets.frame_aroma(self.window)

    def frame_base(self):
        # Show frame base

        self.widgets.frame_base(self.window)
