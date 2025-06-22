# setup.py
from setuptools import setup, find_packages

setup(
    name='mlops-cli',
    version='0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mlops-cli = mlops_cli.main:app',  # if you're using Typer or Click
        ],
    },
    install_requires=[
        'typer[all]',  # or click, argparse, etc.
    ]
)
