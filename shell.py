from pathlib import Path
import shutil
import os

source = Path('calc.py')
dest = Path('src/calc.py')
file = Path("action1.yaml")
directory = Path("src")
current_dir = Path.cwd()
present_dir = os.getcwd()
print(f"Current directory using pathlib: {current_dir}")
print(f"Current directory using os: {present_dir}")
def deletefile(file):
    if file.exists():
        file.unlink()
    else:
        print(f"File {file} does not exist.")

def makedirectory(directory):
    directory.mkdir(exist_ok=True)

def movefile(source, dest):  # Fixed indentation
    if source.exists():
        shutil.move(str(source), str(dest))
    else:
        print(f"Source file {source} does not exist.")

makedirectory(directory)
movefile(source, dest)
deletefile(file)