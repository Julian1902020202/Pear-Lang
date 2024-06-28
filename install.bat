@echo off
rem Überprüfen, ob das Skript als Administrator ausgeführt wird
openfiles >nul 2>&1
if %errorlevel% NEQ 0 (
    echo Please Run this Script as Administrator.
    pause
    exit /b
)

rem Setze den Pfad zur pear.bat Datei
set PEAR_PATH=C:\PearLang\bin\pear.bat

rem System32 Verzeichnis
set SYS32_PATH=%SystemRoot%\System32

rem pear.bat nach System32 kopieren
copy "%PEAR_PATH%" "%SYS32_PATH%\pear.bat"

rem Pfad zur Umgebungsvariable PATH hinzufügen
setx PATH "%PATH%;%SYS32_PATH%"

echo pear was copied to %SYS32_PATH% and added to the PATH.


