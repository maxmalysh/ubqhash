#!/usr/bin/env python
import os
from setuptools import setup, Extension

sources = [
    'src/python/core.c',
    'src/libubqhash/io.c',
    'src/libubqhash/internal.c',
    'src/libubqhash/sha3.c',
    'src/libubqhash/blake2b-ref.c']
if os.name == 'nt':
    sources += [
        'src/libubqhash/util_win32.c',
        'src/libubqhash/io_win32.c',
        'src/libubqhash/mmap_win32.c',
    ]
else:
    sources += [
        'src/libubqhash/io_posix.c'
    ]
depends = [
    'src/libubqhash/ubqhash.h',
    'src/libubqhash/compiler.h',
    'src/libubqhash/data_sizes.h',
    'src/libubqhash/endian.h',
    'src/libubqhash/ubqhash.h',
    'src/libubqhash/io.h',
    'src/libubqhash/fnv.h',
    'src/libubqhash/internal.h',
    'src/libubqhash/sha3.h',
    'src/libubqhash/blake2.h',
    'src/libubqhash/util.h',
]
pyubqhash = Extension('pyubqhash',
                     sources=sources,
                     depends=depends,
                     extra_compile_args=["-Isrc/", "-std=gnu99", "-Wall"])

setup(
    name='pyubqhash',
    author="Max Malysh",
    author_email="github@maxmalysh.com",
    license='GPL',
    version='0.1.25',
    url='https://github.com/maxmalysh/ubqhash',
    download_url='https://github.com/maxmalysh/ubqhash/tarball/master',
    description='Python wrappers for ubqhash',
    ext_modules=[pyubqhash],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
