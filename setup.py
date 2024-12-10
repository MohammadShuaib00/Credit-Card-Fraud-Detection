import os
import sys
from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements_list = []
    try:
        with open(file_path, "r") as file:
            requirements_list = [line.strip() for line in file if line.strip()]
            
            # Remove '-e .' from the requirements
            requirements_list = [req for req in requirements_list if req != '-e .']
    except Exception as e:
        print(f"Error reading requirements file: {e}")
    
    return requirements_list

setup(
    name="creditfrauddetection",
    version="0.1",
    author="Mohammad Shuaib",
    author_email="mohammadshuaib3455@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires='>=3.11',  
    
)
