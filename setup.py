from setuptools import setup, find_packages

ROOT_PACKAGE_NAME = 'Dungeon'


def parse_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name=ROOT_PACKAGE_NAME,
    version='1.0',
    author=['Terentyev Alexey'],
    packages=find_packages(),
    long_description='Dungeon game for TP',
    requirements=parse_requirements()
)