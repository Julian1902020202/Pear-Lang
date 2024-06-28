import subprocess

command = ['pip', 'install', 'auto-py-to-exe']

try:
    subprocess.check_call(command)
    print("installed.")
except subprocess.CalledProcessError as e:
    print("error:", e)

pyinstaller_command = ['pyinstaller', '--noconfirm', '--onefile', '--console', 'dein_skript.py']

try:
    subprocess.check_call(pyinstaller_command)
    print("Compiling successfull")
except subprocess.CalledProcessError as e:
    print("error:", e)

print("exe Logos coming soon!")