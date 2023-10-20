from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'
def get_requierments(file_path:str)->List[str]:
    '''
    thos function will return the list of requiremnets
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)

setup(
    name = 'mlproject',
    version= '0.0.1',
    author= 'hari shantan',
    author_email = 'harishantan99@gmail.com',
    packages=find_packages(),
    install_requires=get_requierments('requierments.txt')
)