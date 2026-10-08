#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="ui-ux-pro-max",
    version="2.6.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={
        "ui_ux_pro_max": [
            "data/*.csv",
            "data/*.json",
            "data/stacks/*.csv",
        ],
    },
    entry_points={
        "console_scripts": [
            "uipro=ui_ux_pro_max.cli:main",
            "ui-ux-pro-max=ui_ux_pro_max.cli:main",
        ],
    },
)
