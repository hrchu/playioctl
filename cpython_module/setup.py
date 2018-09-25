from setuptools import setup, Extension

module = Extension('mt', sources=['mtmodule.c'])

setup(name='mt', ext_modules=[module])
