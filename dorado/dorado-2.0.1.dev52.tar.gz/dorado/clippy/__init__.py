"""
This is the docstring for the examplesubpkg package.  Normally you would
have whatever.py files in this directory implementing some modules, but this
is just an example sub-package, so it doesn't actually do anything.
"""
__all__ = []

from .clippy import *
__all__ += clippy.__all__