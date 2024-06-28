@echo off

set SCRIPT_PATH=c:/PearLang/bin/main.py
set EXECUTE_OPTION=-e

rem Überprüfe, ob ein Argument übergeben wurde
if "%1"=="" (
    echo Usage: pear [file.p]
    exit /b 1
)

rem Überprüfe, ob die Dateiendung .p hat
set FILENAME=%~nx1
set EXTENSION=%~x1
if /i not "%EXTENSION%"==".p" (
    echo Error: Invalid file extension. Only .p files are allowed.
    exit /b 1
)

rem Überprüfe, ob das Ausführungsargument -e ist
if "%2"=="%EXECUTE_OPTION%" (
    rem Führe die Datei exe.py aus
    py C:\PearLang\bin\makeEXE\main.py
) else (
    rem Führe die Standardaktion mit run.py aus
    py %SCRIPT_PATH% %1
)
