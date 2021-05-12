import gzip
import shutil
from pathlib import Path
def create_folder(path):
    Path(path).mkdir(parents=True,exist_ok=True)

file = open("/home/appu/Documents/python_workbench/Roche/path.txt")
for line in file:
    create_folder(line)    

with gzip.open('file.txt.gz', 'rb') as f_in:
    with open('file.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

