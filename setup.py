from setuptools import setup, find_packages

setup(
    name = 'mypackage1',
    version = '0.1',
    package = find_packages(exclude=['tests*']),
    license = 'MIT',
    description = 'EDSA example python package',
    long_description = open('README.md').read(),
    install_requires=['numpy'],
    url = 'https://github.com/alnaschutte/nypackage1 - test.git',
    author = 'Alna Schutte',
    author_email ='schuttealna@gmail.com'
)