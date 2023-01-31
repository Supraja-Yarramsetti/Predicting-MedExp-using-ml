from setuptools import find_packages,setup
from typing import List

requirement_file_name = "requirements.txt"
remove_package = "-e ."
def get_requirements()->List[str]:                                  # convert the list to str 
    with open(requirement_file_name) as requirements_file:
        requirement_list = requirements_file.readline()            #reading the file
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]   #removing the backslash
    
    #removing the packgae

    if remove_package in requirement_list:
        requirement_list.remove(remove_package)
    return requirement_list

#creating setup file
setup(name='Insurance',
      version='0.0.1',
      description='Insurance Industry lavel project',
      author='Supraja Setti',
      author_email='itsmechegg22@gmail.com',
      packages=find_packages(),                                   #check in which folder __init__ file is there
      install_requirements = get_requirements()
    )