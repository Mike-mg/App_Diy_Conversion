# # Main window of program

import tkinter as tk
import sys
from PIL import Image, ImageTk


class MainWindowApp:
    # Main window

    def __init__(self):

        self.window = tk.Tk()
        self.bg = "#f28de2"
        self.background = ImageTk.PhotoImage(
            Image.open("images/background.png"))

    def verify_sysytem_for_icon(self) -> None:
        # Displays the icon according to the system

        if sys.platform.startswith("linux"):
            icon = tk.PhotoImage(file="images/icone.gif")
            self.window.call("wm", "iconphoto", self.window._w, icon)

        elif sys.platform.startswith("win32"):
            self.window.iconbitmap("images/icone.ico")

    def config_windows_tk(self) -> None:
        # Configure the main window

        self.window.title("Diy - Vap")
        self.window.geometry("550x650")
        self.window.resizable(0, 0)

    def image_background(self, window):

        tk.Label(window, image=self.background).place(x=0, y=0)
