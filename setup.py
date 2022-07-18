from setuptools import setup

# name: Name of the package to be uploaded in PyPi
# version: Version of the current package.
# packages: Packages that will be used to create the package.
# include_package_data: To include the package data
# install_requires: External dependencies.
# entry_points: Entry point for the package.
# A egg folder is created when we install this package locally.
# To install the local package, run "pip install --editable ."

setup(
    name="dice-CLI",
    version='1.0',
    packages=['cli', 'cli.commands'],
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points={
        'console_scripts': [
            'breach = cli.cli:cli'
        ]
    }
)
