# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ""

setup(
    long_description=readme,
    name="paranormal",
    version="0.2.2",
    description="Coherent management of large parameter lists in Python",
    python_requires=">3.6",
    author="Schuyler Fried",
    author_email="schuylerfried@gmail.com",
    maintainer="Steven Heidel <steven@heidel.ca",
    license="Apache-2.0",
    packages=["paranormal"],
    package_dir={"": "."},
    package_data={},
    install_requires=["numpy>1.18", "pampy>=0.2.1", "pyyaml>=5.1"],
    extras_require={"dev": ["black==20.*,>=20.8.0.b1", "mock>=3.0", "pytest>=4.4"]},
)
