from typing import List
from setuptools import find_packages,setup 


HYPEN_E_DOT = '-e .'
def get_packages(file_path : str) -> List[str]:
    with open(file_path,'r') as file_obj :
        requiremetns = file_obj.readlines()
        requiremetns = [req.replace('\n','') for req in requiremetns if req != HYPEN_E_DOT ]
    return requiremetns

setup(

    name='ML_PROJECT',
    version='0.0.1',
    author='Harshith',
    author_email='sriharshithg443@gmail.com',
    packages= find_packages(),
    install_requires = get_packages('requirements.txt')
)