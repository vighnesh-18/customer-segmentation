from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT='-e .'
def get_requirements(path:str) -> List[str]:
    '''
    Read the requirements file and return the list of requirements
    '''
    requirements=[]
    with open(path, 'r') as f:
        requirements = f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
name='customer segmentation',
version='0.0.1',
author='Vighnesh Tutikura',
author_email='vighneshtutikura696@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),
)