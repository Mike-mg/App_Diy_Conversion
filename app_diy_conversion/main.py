"""
Entry in App
"""

import window_tkinter


class Main:
    """
    Class main for init the main window
    """

    def __init__(self) -> None:
        """
        Init main window
        """

        self.main_window = window_tkinter.MainWindowApp()


start_window = Main()

start_window.main_window.verify_system_for_icon()
start_window.main_window.config_window()
start_window.main_window.background_window()

start_window.main_window.show_frame_percent_aroma_selected()
start_window.main_window.show_show_frame_quantity_total()
start_window.main_window.show_frame_aroma()
start_window.main_window.show_frame_base()

start_window.main_window.mainloop()
