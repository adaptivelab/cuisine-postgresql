try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
execfile('cuisine_postgresql/version.py')

license_text = open('LICENSE.txt').read()
long_description = open('README.rst').read()


setup(
    author = __maintainer__,
    author_email = __email__,
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
    ],
    data_files=[('', ['LICENSE.txt', 'README.rst'])],
    description = 'Cuisine methods for PosgreSQL',
    install_requires = ['cuisine', 'fabric'],
    license = license_text,
    long_description=long_description,
    name = 'cuisine-postgresql',
    packages = ['cuisine_postgresql'],
    url = 'http://github.com/muhuk/cuisine-postgresql',
    version = __version__,
)
