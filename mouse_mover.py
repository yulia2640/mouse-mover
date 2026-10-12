"""
Mouse Mover - keeps your computer awake by nudging the cursor.

Hotkeys:
    Ctrl+Alt+M  - start / stop moving the mouse
    Ctrl+Alt+Q  - quit the program
"""

import platform
import subprocess
import threading

from pynput import keyboard, mouse

TOGGLE_HOTKEY = "<ctrl>+<alt>+m"
QUIT_HOTKEY = "<ctrl>+<alt>+q"
INTERVAL_SECONDS = 30  # how often to nudge the mouse
NUDGE_PIXELS = 1       # how far to move it (it moves back right away)

cursor = mouse.Controller()
active = threading.Event()
stop = threading.Event()
caffeinate = None  # macOS helper process


def keep_awake(on):
    """Ask the OS directly not to sleep (in addition to moving the mouse)."""
    global caffeinate
    system = platform.system()
    if system == "Windows":
        import ctypes
        ES_CONTINUOUS = 0x80000000
        ES_SYSTEM_REQUIRED = 0x00000001
        ES_DISPLAY_REQUIRED = 0x00000002
        flags = ES_CONTINUOUS
        if on:
            flags |= ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
        ctypes.windll.kernel32.SetThreadExecutionState(flags)
    elif system == "Darwin":
        if on and caffeinate is None:
            caffeinate = subprocess.Popen(["caffeinate", "-d", "-i"])
        elif not on and caffeinate is not None:
            caffeinate.terminate()
            caffeinate = None


def mover_loop():
    while not stop.is_set():
        if active.is_set():
            cursor.move(NUDGE_PIXELS, NUDGE_PIXELS)
            cursor.move(-NUDGE_PIXELS, -NUDGE_PIXELS)
        stop.wait(INTERVAL_SECONDS)


def toggle():
    if active.is_set():
        active.clear()
        keep_awake(False)
        print("Mouse mover: OFF")
    else:
        active.set()
        keep_awake(True)
        print("Mouse mover: ON")


def quit_program():
    stop.set()


def main():
    print("Mouse mover is running.")
    print("  Ctrl+Alt+M  start / stop")
    print("  Ctrl+Alt+Q  quit")
    threading.Thread(target=mover_loop, daemon=True).start()
    hotkeys = keyboard.GlobalHotKeys({
        TOGGLE_HOTKEY: toggle,
        QUIT_HOTKEY: quit_program,
    })
    hotkeys.start()
    try:
        while not stop.wait(0.5):
            pass
    except KeyboardInterrupt:
        stop.set()
    print("Quitting...")
    active.clear()
    keep_awake(False)
    hotkeys.stop()


if __name__ == "__main__":
    main()
