from setuptools import setup, find_packages
from codecs import open
from os import path


ROOT_DIR = path.abspath(path.dirname(__file__))
EXCLUDE_FROM_PACKAGES = ['examples', 'tests', 'tools', 'requirements']

try:
    with open(path.join(ROOT_DIR, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''

setup(
    name='cproto',
    version='0.5',
    description='Chrome Debugging Protocol client',
    long_description=long_description,
    url='https://github.com/asyne/cproto',
    author='Evan K.',
    author_email='cproto+asyne.inout@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='chrome debug client',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    package_data={
        'cproto': ['resources/*.json'],
    },
    install_requires=['websocket-client'],
)
