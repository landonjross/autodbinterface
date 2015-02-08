# -*- coding: utf-8 -*-
from distutils.core import setup
import autodbinterface.__version__

setup(
    name='autodbinterface',
    version=autodbinterface.__version__,
    author='Landon Ross',
    author_email='',
    packages=['autodbinterface'],
    url='https://github.com/landonross/autodbinterface',
    license='LICENSE.txt',
    description='Useful towel-related stuff.',
    long_description=open('README.txt').read()
)
