#  Copyright (c) 2020. This application is owned by Satorihost (Christiansen, Simon).

"""
File: gid-client.py

This program is the client-side component of the larger project named "Get it Done!"
The projects purpose is to provide a tool that helps users prevent procrastination.
This client is what will be run on a users computer.
It will, depending on user settings, only allow certain usage of the computer.

If for some reason the program was to become bugged out and render the user unable to use the computer
and require a restart, there is a built-in kill-switch for the program (CTRL + ALT + G). This will be removed
entirely on production releases.
"""


from multiprocessing import Process


KILL_SWITCH = True

kill_signal = False
environment_data = {}
running_config = {}


def main():
    initialize()
    gui_process = Process(target=gui)
    gui_process.start()


def initialize():
    load_environment_data()
    load_settings()


# Stores info about the host machine in memory as a dictionary
def load_environment_data():
    get_working_directory()
    get_machine_hardware()


# Stores the path of the directory the script was run in if all dependencies are present
def get_working_directory():
    print("get_working_directory not yet defined")


# keyboard layout, mouse / etc., screen resolution, screen size, screen DPI, screen aspect ratio
def get_machine_hardware():
    print("get_machine_hardware not yet defined")


# Stores all settings from gid-client.conf in memory as a dictionary
def load_settings():
    print("load_settings not yet defined")


# Change settings, start work session, see statistics, online ranking
def gui():
    print("gui not yet defined")


if __name__ == '__main__':
    main()
