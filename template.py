# Step 1
import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = 'mlProject'

list_of_files = [
    ## This is for creating a constructor file in a folder. Whenever we want to install our folder as local package. 
    ## For all the folders which we want to use as a local package, we need to add __init__.py file. 
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
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
    "research/trials.ipynb",
    "templates/index.html"
]

# Now in the below code we will be taking 1 file at a time from above list and create it. 
for filepath in list_of_files:
    # In the above list_of_files, we have defined the path with forward slash. If we use linux machine then this works fine however
    # if we use windows machine then in windows, path is defined using backward slash. To make our code compatible with all the
    # Operating systems, we will put the filepath inside Path. What Path from Pathlib does is - it converts the path into the format 
    # that the operating system supports. In this way we don't have to worry about all these things. 
    filepath = Path(filepath)
    # Now we want to separate our folder from file in the list_of_files. Reason being, we will first need to create folders and then
    # the files will be created inside it. To do this we will use split as below - 
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating Directory: {filedir} for the file: {filename}")
    # to create file we will need to check two conditions - first is if the file exists or not. If it does not exist then it is 
    # easy we just create the file. However if it exists then we check what is the size of the file using getsize function. 
    # this helps in ensuring that id the file exists and has size > 0 then do not create it. If we create file in this scenario
    # then our contents will be wiped out which we do not want
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open (filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging(f"{filename} already exists")
# Step 1 complete

# Step 2: In terminal peform the following:
# python template.py
# Step 2 complte. This will create the folder structure

# Step3 : To run into terminal for creating virtual environment
# '''bash
# conda create -n mlproj python 3.8 -y
#conda activate mlproj
# '''
# Step 3: Complete

# Step 4: Add all the libraries that will be needed in the requirements.txt file. Got to requirements.txt to see this.
# After this add the contents in the setup.py file which will be step 5.
# Step 4 complete 


# Step 6: After writing all the needed libraries in requirements.txt (step 4). We need to execute the below 
# command in terminal
# pip install -r requirements.txt
# Step 6 complete