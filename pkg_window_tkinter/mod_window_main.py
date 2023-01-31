# Main window of program

import tkinter as tk
import sys
from PIL import Image, ImageTk
import pkg_widgets


class MainWindowApp(tk.Tk):
    # Main window

    def __init__(self):
        super().__init__()

        self.bg = "#f28de2"
        self.background = ImageTk.PhotoImage(
            Image.open("images/background.png"))

        self.widgets = pkg_widgets.FramesWidgets()

    def verify_system_for_icon(self) -> None:
        # Displays the icon according to the system

        if sys.platform.startswith("linux"):
            icon = tk.PhotoImage(file="images/icone.gif")
            self.call("wm", "iconphoto", self._w, icon)

        elif sys.platform.startswith("win32"):
            self.iconbitmap("images/icone.ico")

    def config_window(self) -> None:
        # Configure the main window

        self.title("Diy - Vap")
        self.geometry("522x575")
        self.resizable(0, 0)

    def background_window(self) -> None:
        # Background window

        tk.Label(self, image=self.background).place(x=1, y=0)

    def show_frame_percent_aroma_selected(self) -> None:
        # Show frame select aroma percent

        self.widgets.frame_percent_aroma_selected(self)

    def show_show_frame_quantity_total(self) -> None:
        # Show frame quantity

        self.widgets.frame_quantity_total(self)

    def show_frame_aroma(self) -> None:
        # Show frame aroma

        self.widgets.frame_aroma(self)

    def show_frame_base(self) -> None:
        # Show frame base

        self.widgets.frame_base(self)
