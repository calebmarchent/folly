#!/usr/bin/env python3

# Example calling command:
# $./setup.py build_ext --inplace


from setuptools import setup, Extension
from Cython.Build import cythonize
from Cython.Compiler import Options
import os

Options.fast_fail = True

ext = Extension("folly.executor",
   sources=['python/executor.pyx'],
   include_dirs=[os.getcwd()+"/..", os.getcwd()],
   libraries=['folly', 'glog', 'double-conversion', 'iberty'])

setup(name="folly",
      ext_package="folly",
      version='0.0.1',
      language="c++",
      zip_safe=False,
      ext_modules = cythonize([ext],
                              compiler_directives={'language_level': 3,}))
