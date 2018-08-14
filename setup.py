"""scrum python package configuration."""

from setuptools import setup

setup(
    name='scrum',
    version='0.1.0',
    packages=['scrum'],
    include_package_data=True,
    install_requires=[
        'flask',
        'html5validator',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'nodeenv',
        'sh',
        'Flask-Testing',
        'selenium',
        'requests',
        'arrow'
    ],
)
