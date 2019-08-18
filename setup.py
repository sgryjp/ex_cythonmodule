"""Setup script for stopwatches."""
from setuptools import setup  # noqa
from Cython.Build import cythonize


setup(
    ext_modules=cythonize("./*.pyx"),
)
