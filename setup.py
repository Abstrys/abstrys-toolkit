#!/usr/bin/env python
from distutils.core import setup

script_names = [
    'scripts/cleanjson',
    'scripts/fix_filenames',
    'scripts/rompy',
    'scripts/s3lod',
    'scripts/s3pub',
    'scripts/snippetize',
    'scripts/srep',
    ]

setup(name='abstrys-toolkit',
      description='Useful command-line tools and scripts.',
      version='1.03',
      requires=['json', 'boto', 'PyYAML'],
      scripts=script_names,
      author='Eron Hennessey',
      author_email='eron@abstrys.com',
      url='https://github.com/Abstrys/abstrys-toolkit',
      )
