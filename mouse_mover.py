"""
Mouse Mover - keeps your computer awake by nudging the cursor.

Hotkeys:
    Ctrl+Alt+M  - start moving the mouse
    Ctrl+Alt+Q  - quit the program

Any mouse click or key press stops it again.
"""

import platform
import subprocess
import threading
import time

from pynput import keyboard, mouse

START_HOTKEY = "<ctrl>+<alt>+m"
QUIT_HOTKEY = "<ctrl>+<alt>+q"
INTERVAL_SECONDS = 30  # how often to nudge the mouse
NUDGE_PIXELS = 1       # how far to move it (it moves back right away)
GRACE_SECONDS = 1      # ignore input right after starting (the hotkey itself)

SYSTEM = platform.system()

cursor = mouse.Controller()
active = threading.Event()
stop = threading.Event()
started_at = 0.0


def beep(frequency):
    """Short sound so you know what happened (there is no window)."""
    if SYSTEM == "Windows":
        import winsound
        winsound.Beep(frequency, 150)


def tell_os_user_is_active():
    """Reset the OS idle timer directly, in addition to moving the mouse."""
    if SYSTEM == "Windows":
        import ctypes
        ES_SYSTEM_REQUIRED = 0x00000001
        ES_DISPLAY_REQUIRED = 0x00000002
        ctypes.windll.kernel32.SetThreadExecutionState(
            ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)
    elif SYSTEM == "Darwin":
        subprocess.Popen(["caffeinate", "-u", "-t", "1"])


def mover_loop():
    while not stop.is_set():
        if active.is_set():
            cursor.move(NUDGE_PIXELS, NUDGE_PIXELS)
            cursor.move(-NUDGE_PIXELS, -NUDGE_PIXELS)
            tell_os_user_is_active()
        stop.wait(INTERVAL_SECONDS)


def activate():
    global started_at
    if not active.is_set():
        started_at = time.monotonic()
        active.set()
        print("Mouse mover: ON")
        beep(1000)


def deactivate(*_):
    if active.is_set() and time.monotonic() - started_at > GRACE_SECONDS:
        active.clear()
        print("Mouse mover: OFF")
        beep(500)


def on_click(x, y, button, pressed):
    if pressed:
        deactivate()


def quit_program():
    stop.set()


def main():
    print("Mouse mover is running.")
    print("  Ctrl+Alt+M  start (any click or key press stops it)")
    print("  Ctrl+Alt+Q  quit")
    threading.Thread(target=mover_loop, daemon=True).start()
    listeners = [
        keyboard.GlobalHotKeys({
            START_HOTKEY: activate,
            QUIT_HOTKEY: quit_program,
        }),
        keyboard.Listener(on_press=deactivate),
        mouse.Listener(on_click=on_click),
    ]
    for listener in listeners:
        listener.start()
    try:
        while not stop.wait(0.5):
            pass
    except KeyboardInterrupt:
        stop.set()
    print("Quitting...")
    active.clear()
    for listener in listeners:
        listener.stop()


if __name__ == "__main__":
    main()
