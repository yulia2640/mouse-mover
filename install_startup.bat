@echo off
rem Installs Mouse Mover so it starts automatically when you log in to Windows.

set "STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
set "SCRIPT=%~dp0mouse_mover.py"

echo Installing the pynput library...
py -m pip install -r "%~dp0requirements.txt" || python -m pip install -r "%~dp0requirements.txt"

rem A tiny .vbs launcher starts the program with no console window.
> "%STARTUP%\MouseMover.vbs" (
    echo Set shell = CreateObject^("WScript.Shell"^)
    echo On Error Resume Next
    echo shell.Run "pyw ""%SCRIPT%""", 0, False
    echo If Err.Number ^<^> 0 Then
    echo     Err.Clear
    echo     shell.Run "pythonw ""%SCRIPT%""", 0, False
    echo End If
)

rem Start it now as well, so you don't have to log out and in.
start "" wscript "%STARTUP%\MouseMover.vbs"

echo.
echo Done! Mouse Mover is running and will start every time you log in.
echo   Ctrl+Alt+M  start moving the mouse
echo   Any click or key press stops it
echo   Ctrl+Alt+Q  quit
echo.
pause
