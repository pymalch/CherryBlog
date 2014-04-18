# -*- coding: utf-8 -*-
import os
import re
from setuptools import find_packages
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# reading cherryblog version without importing any modules from that package
with open(os.path.join(os.path.dirname(__file__), 'cherryblog', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)

dependencies = [
    'cherrypy>=3.2.5',
    'pymlconf>=0.3.10',
    'CherrypyMako>=0.3.1',
    'CherrypyElixir>=0.5.1'
]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="CherryBlog",
    version=package_version,
    author="Vahid Mardani",
    author_email="vahid.mardani@gmail.com",
    url="http://github.com/pylover/cherryblog",
    description="Simplt blogging system using cherrypy",
    packages= find_packages(exclude=['ez_setup']),
    platforms=["any"],
    long_description=read('README.rst'),
    install_requires=dependencies,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: Freeware",
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technolog',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers'
    ],
    test_suite='pymlconf.tests',
)
