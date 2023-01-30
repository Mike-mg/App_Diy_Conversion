# Entry program

import pkg_window_tkinter


class Main:
    # Entry program

    def __init__(self) -> None:
        self.main_window = pkg_window_tkinter.MainWindowApp()


start_window = Main()

start_window.main_window.verify_sysytem_for_icon()
start_window.main_window.config_window()
start_window.main_window.image_background()

start_window.main_window.frame_dosage()
start_window.main_window.frame_quantity()
start_window.main_window.frame_aroma()
start_window.main_window.frame_base()

start_window.main_window.window.mainloop()
