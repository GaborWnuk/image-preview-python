#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    setup.py
    ~~~~~~~~

    Image Preview creation python library to create low footprint image previews,
    convenient to use as base64 data in your REST / GraphQL API payload

    :copyright: (c) 2016 by GaborWnuk.
    :license: see LICENSE for more details.
"""

import codecs
import os
import re
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """Taken from pypa pip setup.py:
    intentionally *not* adding an encoding option to open, See:
       https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    """
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='imagepreview',
    version=find_version("imagepreview", "__init__.py"),
    description='Image Preview creation python library to create low footprint '\
                'image previews, convenient to use as base64 data in your REST '\
                '/ GraphQL API payload.',
    long_description=read('README.md'),
    classifiers=[
        ],
    author='Gabor Wnuk',
    author_email='gabor.wnuk@me.com',
    url='https://github.com/GaborWnuk/image-preview-python',
    download_url='https://github.com/GaborWnuk/image-preview-python/tarball/%s' % find_version("imagepreview", "__init__.py"),
    packages=[
        'imagepreview'
        ],
    platforms='any',
    license='MIT',
    install_requires=[
        'pyflakes>=0.8.1',
        'virtualenv>=1.11.6',
        'pep8>=1.5.7',
        'Pillow==3.4.2'
        ]
)
