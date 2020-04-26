# gui_builder.py
import tkinter as tk
import pygubu


class GidClientGUI:

    def __init__(self):
        # 1: Create a builder
        self.builder = builder = pygubu.Builder()

        # 2: Load an ui file
        builder.add_from_file('gid-client-gui.ui')

        # 3: Create the mainwindow
        self.mainwindow = builder.get_object('Frame1')

    def run(self):
        self.mainwindow.mainloop()


"""
if __name__ == '__main__':
    app = GidClientGUI()
    app.run()
"""