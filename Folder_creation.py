from pathlib import Path
def create_folder(path):
    Path(path).mkdir(parents=True,exist_ok=True)

file = open("/home/appu/Documents/python_workbench/Roche/path.txt")
for line in file:
    create_folder(line)    
