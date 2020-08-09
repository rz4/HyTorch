#!/usr/bin/env python3

__author__ = 'Rafael Zamora-Resendiz, rzamoraresendiz@protonmail.com'

from setuptools import setup, find_packages

setup(
    name="mino",
    version="0.0.9",
    description="PyTorch Meta-Programming Using the Lisp Dialect Hy",
    license="MIT",
    keywords="Hy PyTorch Meta",
    packages=find_packages(exclude=["images", "jupyter", "notebooks"]),
    package_data={
        'mino': ['*.hy', '*.py'],
    },
    install_requires = ["hy", "torch",  "dill"],
)
