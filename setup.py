#!/usr/bin/env python3
"""
Setup script for Fouad Box
"""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="fouadbox",
    version="1.0.0",
    author="Fouad Zulof",
    author_email="zalaffouad37@gmail.com",
    description="Advanced Security Toolkit for Penetration Testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fouadzulof/fouadbox",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "fouadbox=fouadbox:main",
        ],
    },
    include_package_data=True,
    keywords="security pentesting hacking cybersecurity ethical-hacking",
    project_urls={
        "Bug Reports": "https://github.com/fouadzulof/fouadbox/issues",
        "Source": "https://github.com/fouadzulof/fouadbox",
    },
)
