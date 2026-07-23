'''  
      the set up file is an essential part of packageing and
      distributing python projects.it is used by setuptools
      or disutils in older python versions to define the configuration
      of your project,such as its metadata,dependencies,and more
'''

from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirement_list:List[str]=[]
    try:
        with open('requirement.txt','r') as file:
            # read line from the file
            lines=file.readlines()
            ## process each line
            
            for line in lines:
                requirement=line.strip()
                # ignore the empty lines and -e.
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirement.txt file is not found")
    return requirement_list 

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="keerthi konari",
    author_email="keerthikonari430@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements())



