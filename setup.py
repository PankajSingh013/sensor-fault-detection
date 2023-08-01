from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return a list of requirment packages
    '''
    requirement_list:List[str] = []
    #write a code to read the requirements.txt file and return a list of packages
    return requirement_list

setup(
    name='sensor',
    version='0.0.1',
    author_email='amitbisht25@gmail.com',
    packages= find_packages(),
    install_requires=get_requirements(), #["pymongo==4.2.0"],
)