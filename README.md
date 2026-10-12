# Mouse Mover

A tiny program that keeps your computer awake by nudging the mouse cursor
every 10 seconds. It starts with Windows and waits quietly in the background.

| Action                       | What happens                       |
| ---------------------------- | ---------------------------------- |
| `Ctrl+Alt+M`                 | Start keeping the computer awake (high beep) |
| Any mouse click or key press | Stop (low beep)                    |
| `Ctrl+Alt+Q`                 | Quit the program completely        |

The cursor moves 1 pixel and straight back, so you won't notice it. It also
tells Windows directly not to sleep or turn off the screen.

## Install on Windows (starts automatically)

1. Install [Python 3](https://www.python.org/downloads/). In the installer,
   tick **"Add Python to PATH"**.
2. Download this folder and keep it somewhere permanent (e.g. `Documents\Mouse-mover`).
3. Double-click **`install_startup.bat`**.

That's it — it is running now and will start every time you log in.
There is no window; listen for the beeps.

To remove it from startup, double-click **`uninstall_startup.bat`**.

> If you move the folder later, run `install_startup.bat` again.

## Run manually

```
pip install -r requirements.txt
python mouse_mover.py
```

## Settings

Edit the top of `mouse_mover.py` to change the hotkeys, the interval
(`INTERVAL_SECONDS`) or how far the mouse moves (`NUDGE_PIXELS`).
