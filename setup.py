from setuptools import setup, find_packages
import re
import os
import io

this_directory = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def get_version(package):
    """Return package version as listed in `__version__` in `init.py`."""
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name='pyshac',
    version=get_version("pyshac"),
    packages=find_packages(),
    url='https://github.com/titu1994/pyshac',
    download_url='https://github.com/titu1994/pyshac',
    license='MIT',
    author='Somshubra Majumdar',
    author_email='titu1994@gmail.com',
    description='Python library which implements Successive Halving and Classification algorithm',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['numpy>=1.15.2',
                      'scikit-learn>=0.19.1',
                      'pandas>=0.23.4',
                      'joblib>=0.12.5',
                      'loky>=2.3.1',
                      'cloudpickle>=0.6.1',
                      'six>=1.11.0',
                      'xgboost>=0.80',
                      'matplotlib>=3.0.0; python_version > "3.0"'],
    extras_require={
        'tests': ['pytest', 'coverage', 'pytest-cov', 'codecov', 'matplotlib'],
    },
    classifiers=(
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
    zip_safe=False,
    test_suite="tests",
)
