# setup.py
from setuptools import setup

setup(
    name='mlops-cli',
    version='0.1',
    packages=['mlops_cli'],
    entry_points={
        'console_scripts': [
            'mlops-cli = mlops_cli.main:app',  # if you're using Typer or Click
        ],
    },
    install_requires=[
        'typer[all]',  # or click, argparse, etc.
    ]
)
