try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Sudoku plaything',
    'author': 'Tom Fawssett',
    'url': '',
    'download_url': '',
    'author_email': '',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['sudoku'],
    'scripts': ['bin/sudoku-test'],
    'name': 'sudoku'
}

setup(**config)
