try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'projectname'
    'version': '0.1',
    'description': 'My Project',
    'author': 'My Name',
    'author_email': 'My email.',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'packages': ['NAME'],
    'install_requires': ['nose'],
    'scripts': [],
}

setup(**config)
