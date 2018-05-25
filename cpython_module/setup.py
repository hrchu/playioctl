import os
from setuptools import setup, Extension

module = Extension('spam', sources=['spammodule.c'])

setup(name='spam', ext_modules = [module])

