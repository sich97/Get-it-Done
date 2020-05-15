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
import os
from pynput import keyboard
import time

KILL_SWITCH = True
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='a')},
    {keyboard.Key.shift, keyboard.KeyCode(char='A')}
]


def main():
    print("Start of main")

    running_config, run_signal, blocker_process = initialize()

    print("Before starting menu")
    while not run_signal:
        menu(running_config, run_signal)


def initialize():
    print("Creating run_signal")
    run_signal = Signal("run_signal", True)

    print("Loading settings")
    # load_environment_data()
    running_config = load_settings()

    # Setting up the kill switch
    if KILL_SWITCH:
        print("Setting up kill switch")
        kill_switch_process = Process(target=kill_switch(run_signal))
        kill_switch_process.start()

    # Starts the blocker as a separate process
    print("Starts the blocker process")
    blocker_process = Process(target=blocker(running_config, run_signal))
    blocker_process.start()

    print("End of initialization")
    return running_config, run_signal, blocker_process


def kill_switch(run_signal):
    print("Start of kill switch")
    current = set()

    def on_press(key):
        print("Key pressed")
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.add(key)
            if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
                print("Hot-key detected")
                print("Run signal was: " + str(run_signal.get_state()))
                run_signal.set_state(False)
                print("Run signal is now: " + str(run_signal.get_state()))

    def on_release(key):
        print("Key released")
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.remove(key)

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


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
    settings = {"Duration hours": 0, "Duration minutes": 0, "Duration seconds": 0}
    return settings


def menu(running_config, run_signal):
    # os.system('cls' if os.name == 'nt' else 'clear')
    print_menu_options()
    menu_choice = int(input("Please input the corresponding integer of your decision: "))
    if menu_choice == 1:
        run_signal.set_state(True)

    if menu_choice == 2:
        while not run_signal.get_state():
            print("Test")


def print_menu_options():
    print("Welcome to the command-line for Get-it-Done!")
    print("Here are some options for you:")
    print("1:\tStart session\n")
    print("2:\tTest\n")


def blocker(running_config, run_signal):
    print("Start of blocker process")
    while True:
        print("Wait for 1 second")
        time.sleep(1)
        print("Checks run signal")
        while run_signal.get_state():
            print("Run signal is: " + str(run_signal.get_state()))


class Signal:
    def __init__(self, name, initial_state):
        self.state = initial_state
        self.name = name

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        old_state = self.state
        self.state = new_state
        print(self.name + " was changed from " + str(old_state) + " to " + str(new_state))


if __name__ == '__main__':
    main()
