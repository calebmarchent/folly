#!/usr/bin/env python3

# Example calling command:
# $./setup.py build_ext --inplace


from setuptools import setup, Extension
from Cython.Build import cythonize
from Cython.Compiler import Options
import os

Options.fast_fail = True

ext = Extension("folly.executor",
                sources=['folly/executor.pyx'],
   include_dirs=[os.getcwd()+"/..", os.getcwd()],
   libraries=['glog', 'double-conversion', 'iberty'])

#if not os.path.isdir('folly'):
#    os.makedirs('folly')
#
#for f in ['executor.pxd',
#          'executor.pyx',
#          'futures.pxd',
#          '__init__.pxd',
#          'AsyncioExecutor.h']:
#    if not os.path.exists('folly/'+f):
#        os.symlink('../python/'+f, 'folly/'+f)

setup(name="folly",
      version='0.0.1',
      packages=['folly'],
      package_data={ "": ['*.pxd', '*.h'] },
      language="c++",
      zip_safe=False,
      ext_modules = cythonize([ext],
                              compiler_directives={'language_level': 3,}))
