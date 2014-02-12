try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'First example of installing my own module',
    'author': 'Ian Polding',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'ipolding@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['nameprinter'],
    'scripts': ['bin/ExecNamePrinter.py'],
    'modules': ['re'],
    'name': 'python-nameprinter'
}

setup(**config)
