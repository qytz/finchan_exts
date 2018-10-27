#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# 'setup.py publish' shortcut.
# if sys.argv[-1] == 'publish':
#     os.system('python setup.py sdist bdist_wheel')
#     os.system('twine upload dist/*')
#     sys.exit()

with open('README.rst') as readme_file:
    readme = readme_file.read()

about = {}
with open(os.path.join(here, 'finchan_exts', '__version__.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=find_packages(where=here, exclude=('tests',)),
    package_data={'': ['LICENSE']},
    package_dir={'finchan_exts': 'finchan_exts'},
    include_package_data=True,
    python_requires=">=3.6*",
    install_requires=[
        'click',
        'uvloop',
        'python-dateutil',
        'ruamel.yaml'],
    license=about['__license__'],
    zip_safe=True,
    keywords='finchan',
    classifiers=[
        'Framework :: Robot Framework',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6'
    ],
)
