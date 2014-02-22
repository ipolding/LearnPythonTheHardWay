try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Scanner project',
    'author': 'Ian Polding',
    'author_email': 'ipolding@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['lexicon'],
    'scripts': [],
    'name': 'ex48'
}

setup(**config)
