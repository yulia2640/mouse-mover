# Mouse Mover

A tiny program that keeps your computer awake by nudging the mouse cursor
every 30 seconds. You switch it on and off with a keyboard shortcut.

| Hotkey         | Action                    |
| -------------- | ------------------------- |
| `Ctrl+Alt+M`   | Start / stop moving mouse |
| `Ctrl+Alt+Q`   | Quit                      |

The cursor moves 1 pixel and straight back, so you won't notice it while working.
On Windows and macOS it also tells the system directly not to sleep.

## Setup

1. Install [Python 3](https://www.python.org/downloads/) (on Windows, tick
   "Add Python to PATH" in the installer).
2. Install the one dependency:

   ```
   pip install -r requirements.txt
   ```

## Run

```
python mouse_mover.py
```

Leave the window open (you can minimize it), then press `Ctrl+Alt+M` to start.

On Windows you can run it without a console window by double-clicking it after
renaming it to `mouse_mover.pyw`.

### macOS note

The first time you run it, macOS will ask for permission. Allow your terminal
(e.g. Terminal or iTerm) in **System Settings → Privacy & Security →
Accessibility** and **Input Monitoring**, then restart the program.

## Settings

Edit the top of `mouse_mover.py` to change the hotkeys, the interval
(`INTERVAL_SECONDS`) or how far the mouse moves (`NUDGE_PIXELS`).
