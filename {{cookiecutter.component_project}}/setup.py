#!/usr/bin/env python

# Adding our unit testing standards
import sys
sys.path.append('../standards')

from setuptools import setup

# The actual setup fucntion call:
setup(
    name="{{ cookiecutter.component_project.replace(' ', '-') }}",
    version='0.1.dev0',
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.email }}",
    url="{{ cookiecutter.url }}",
    description="{{ cookiecutter.description }}",
    package_dir={
        "": "src",
        # ...
    },
    # Can also be automatically generated using setuptools.findpackages
    packages=[
        "{{ cookiecutter.component_project }}",
        # ...
    ],
    package_data={
        # "{{ cookiecutter.component_project }}":[
        #     "filename.ext",
        #     # ...
        # ]
    },
    entry_points={
        # "console_scripts":[
        #     "executable_name = namespace.path:function",
        #     # ...
        # ],
    },
    # Adding the test suite for the project
    test_suite='tests.test_{{ cookiecutter.component_project }}',
)