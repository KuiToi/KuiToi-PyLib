# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

packages = ['KuiToi']

requires = []

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python -m build')
    os.system('python -m twine upload --repository testpypi dist/*')
    os.system('python -m twine upload --repository pypi dist/*')
    sys.exit()

about = {}
with open(os.path.join(here, packages[0], '__version__.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'KuiToi': 'KuiToi'},
    include_package_data=True,
    install_requires=requires,
    license=about['__license__'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Natural Language :: Russian",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Source': about['__url__'],
    },
    python_requires=">=3.7",
)