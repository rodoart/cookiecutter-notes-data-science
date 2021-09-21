import os
import subprocess
import pathlib


CURRENT_DIR = pathlib.Path(".").resolve()

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"Creating virtual enviroment...{RESET_ALL}")

enviro_path = CURRENT_DIR.joinpath("environment.yml")
os.system(f'conda env create --file "{enviro_path}"')

print(f"Starting virtual envirmoment...{RESET_ALL}")
os.system('conda activate {{ cookiecutter.project_slug }}')

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")