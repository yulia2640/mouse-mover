@echo off
rem Stops Mouse Mover from starting when you log in to Windows.

del "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\MouseMover.vbs" 2>nul

echo Mouse Mover will no longer start with Windows.
echo If it is running right now, press Ctrl+Alt+Q to quit it.
echo.
pause
