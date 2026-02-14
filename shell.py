from pathlib import Path
import shutil

source = Path('calc.py')
dest = Path('src/calc.py')
file = Path("action1.yaml")
directory = Path("src")

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