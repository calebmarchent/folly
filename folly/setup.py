#!/usr/bin/env python3

# Do not call directly, use cmake
#
# Cython requires source files in a specific structure, the structure is
# created as tree of links to the real source files.

from setuptools import setup, Extension
import os
from setuptools.command.build_ext import build_ext as _build_ext
from distutils.file_util import copy_file

class heresoneimadeearlier(_build_ext):

    def build_extension(self, ext):
        copy_file(
            ext.sources[0],
            self.get_ext_fullpath(ext.name),
            verbose=self.verbose,
            dry_run=self.dry_run
        )

# Extension: filename created by cmake
extensions = [
    Extension("folly.executor", sources=["../executor.so"]),
]

setup(name="folly",
      cmdclass={'build_ext': heresoneimadeearlier},
      version='0.0.1',
      packages=['folly'],
      package_data={"": ['*.pxd', '*.h']},
      zip_safe=False,
      ext_modules=extensions
)
