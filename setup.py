#!/usr/bin/env python

# Setup script for abstrys-toolkit.
#
# For more information, go to https://github.com/Abstrys/abstrys-toolkit

from setuptools import setup, find_packages

setup(
    name = 'abstrys-toolkit',
    version = '1.1',
    author = 'Eron Hennessey',
    author_email = 'eron@abstrys.com',
    url = 'https://github.com/Abstrys/abstrys-toolkit',
    description = """
        Useful command-line tools and scripts, designed for technical writing and
        publication.
        """,
    license = 'BSD',
    keywords = ('aws camel2snake cleanjson clinks command-line fix-filenames'
        + 'music-album-renamer rompy s3 s3search snippetize srep tools'),

    packages = find_packages(),

    entry_points={
        'console_scripts': ['s3search = abstrys_toolkit.cmd_s3search:main']
    },

    install_requires = ['boto3'],
)

