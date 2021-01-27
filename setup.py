#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import find_packages, setup  # type: ignore


def read(fname):
    # type: (str) -> str
    with open(os.path.join(os.path.dirname(__file__), fname), "rb") as fid:
        return fid.read().decode("utf-8")


PYTHON_VERSION = sys.version_info.major
ENTRYPOINT = "neovim_sh.__main__:main"

setup(
    name="neovim-sh",
    version="0.1",
    description="Neovim wrapper project to install as a script",
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    url="https://github.com/miki725/neovim-sh",
    license="MIT",
    packages=find_packages(),
    install_requires=["neovim"],
    entry_points={
        "console_scripts": [
            "neovim{PYTHON_VERSION}.sh = {ENTRYPOINT}".format(**locals()),
        ],
    },
    keywords=" ".join(["neovim"]),
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
    ],
)
