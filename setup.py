from typing import List

from setuptools import find_packages, setup


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [r.replace("\n", "") for r in requirements]
    if "-e ." in requirements:
        requirements.remove("-e .")

    return requirements


setup(
    name="domain-classifer",
    version="0.0.1",
    author="Rekib",
    author_email="rkb.ra0025@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
