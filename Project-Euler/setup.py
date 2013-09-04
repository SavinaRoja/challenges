"""
This is the setup file to install my Project Euler shared method module.
"""

from distutils.core import setup, Extension

c_module = Extension('pemaths/c_maths',
                     sources = ['pemaths/c_maths.c'],
                     libraries = ['gmp'])

setup (name = 'ProjectEuler',
       version = '0.1',
       description = 'This installs my Project Euler share method module',
       author='Paul Barton',
       packages = ['pemaths'],
       ext_modules = [c_module])
