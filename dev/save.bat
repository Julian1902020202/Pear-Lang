@echo off
set SCRIPT_PATH=c:/jsharp/bin/run.py
if "%1"=="" (
    echo Usage: jsharp.bat [file.jsharp]
    exit /b 1
)
py %SCRIPT_PATH% %1
