from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path : str) -> List[str]:

    '''
    This function will return the list of requirements
    '''

    reuirements = []

    with open(file_path) as file_obj:
        reuirements = file_obj.readlines()
        reuirements = [req.replace("\n", "") for req in reuirements]

        if HYPEN_E_DOT in reuirements:
            reuirements.remove(HYPEN_E_DOT)
    return reuirements

setup(
    name = 'project1',
    version = '0.0.1',
    author= 'abhay',
    author_email= 'abhay@example.com',
    packages= find_packages(),
    install_requires= get_requirements('requirement.txt')
)