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

        self.widgets = pkg_widgets.FramesWidgets(self.window)

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

    def image_background(self, window):

        tk.Label(window, image=self.background).place(x=0, y=0)

    def frame_dosage(self):
        # Show select dosage percent

        self.widgets.frame_dosage()

    def frame_quantity(self):
        # Show select dosage percent

        self.widgets.frame_quantity()

    def frame_aroma(self):
        # Show select dosage percent

        self.widgets.frame_aroma()

    def frame_base(self):
        # Show select dosage percent

        self.widgets.frame_base()
