import os
from pathlib import Path #this librabry take care of the wrong path or worng slase(/,\)

package_name="mongodb_connect" #initilize the pacage name


list_of_files=[
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py", #inside the pacage folder we have init file
    f"src/{package_name}/mongo_crud.py", #inside mongo have mongodb_crud.py
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",#all test cases
    "tests/integration/__init__.py",
    "tests/integration/int.py",#intergaration testing
    "init_setup.sh",
    "requirements.txt", 
    "requirements_dev.txt",#requiment file when development environment
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiments.ipynb", 
   #they all files create fro the making python package files
]

for filepath in list_of_files: #run the loop so that all the files are make on the githubs
    filepath=Path(filepath) #give the file path (.github/workflow/.gitkey)
    filedir,dilename=os.path.split(filepath) # split the directory and file name
    if filedir !="": #file directory is not empty
        os.makedirs(filedir,exist_ok=True) # make the directory od the name is filedir and exist is true means perments make the directory
        #logging.info(f"Creating directory:{filedir} for file:{filename}") # print the directory name and the file name
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass #create an empty file
    



