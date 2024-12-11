from setuptools import find_packages, setup
from typing import List

hyphen_e='-e .'

def get_requirements(file_path:str)->List[str]:
    """
    This Function will returns the list of all libraries 
    """
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        #requirements=[i.replace('\n',' ') for i in requirements]
        requirements=[i.strip() for i in requirements]

        if hyphen_e in requirements:
            requirements.remove(hyphen_e)

setup(
    name='mlproject',
    version='0.0.01',
    author='Dnyanesh',
    Author_email='dnyan.bs@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)