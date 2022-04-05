# -*- coding: utf-8 -*-
"""
Copyright (C) 2020 by Timothy C. Quinn
This software may be modified and distributed under the terms of
the BSD 3-Clause license. See the LICENSE file for details.
"""

# Deploy to PyPi
# % python3 setup.py sdist bdist_wheel
# % python3 -m twine upload --skip-existing dist/*
from setuptools import setup
import os

VERSION = "0.1"

def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()

# see https://pypi.org/classifiers/
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: BSD License',
    'Operating System :: POSIX :: Linux',
    'Operating System :: POSIX :: BSD',
    'Operating System :: POSIX :: SunOS/Solaris',
    'Operating System :: MacOS :: MacOS X',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: System :: Filesystems',
    'Topic :: Utilities',
]

setup(
    name="tiotrap",
    description="Helper For Capturing Text IO Streams like stdout, stderr",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Timothy C. Quinn",
    url="https://github.com/JavaScriptDude/tiotrap",
    project_urls={
        "Issues": "https://github.com/JavaScriptDude/tiotrap/issues",
        "CI": "https://github.com/JavaScriptDude/tiotrap/actions",
        "Changelog": "https://github.com/JavaScriptDude/tiotrap/releases",
    },
    license="BSD-3-Clause",
    version=VERSION,
    packages=["tiotrap"],
    install_requires=[],
    extras_require={},
    python_requires=">=3.7",
    classifiers=CLASSIFIERS,
)
