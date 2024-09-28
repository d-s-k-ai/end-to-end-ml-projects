import os
from pathlib import Path  # To handle path manipulation
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

project_name = 'ml_project'

# List of files to be created
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trains.ipynb",
    "templates/index.html"
]

# Create the directories and files
for filepath in list_of_files:
    filepath = Path(filepath)

    # Get the directory and file name
    filedir = filepath.parent
    filename = filepath.name

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create an empty file if it doesn't exist or if its size is 0
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
