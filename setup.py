## Step 5 : Create this setup.py file

import setuptools

# Below code is not a mandatory code. We can ignore this too. All this is doing is reading out README.md file. 
with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Red-Wine-Prediction"
AUTHOR_USER_NAME = "Radhika5062"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "radhikamaheshwari26@gmail.com"

# Using the below code, we are setting up our folders as local packages. 
# When we try to import packages then this code will help find the __init__.py file in each folder and then this 
# will allow us to import methods from one folder/package into another. 
# IMP: To install setup.py we need to add -e / in the requirements.txt file. 

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for ML App",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where = "src")

)

# Step 5 Complete