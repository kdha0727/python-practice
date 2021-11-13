# setup.py

from distutils.core import setup, Extension

setup(
    name="customlib",
    version="1.0",
    description="desc",
    ext_modules=[Extension("customlib", sources=["customlib_src.c"])]
)
