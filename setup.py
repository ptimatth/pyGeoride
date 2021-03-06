# pylint: disable=invalid-name, exec-used
"""Setup georideapilib package."""
from __future__ import absolute_import

import os
import sys

from setuptools import setup

sys.path.insert(0, '.')

CURRENT_DIR = os.path.dirname(__file__)

# to deploy to pip, please use
# make pythonpack
# python setup.py register sdist upload
# and be sure to test it firstly using
# "python setup.py register sdist upload -r pypitest"
setup(
    name='georideapilib',
    packages=['georideapilib'],  # this must be the same as the name above
    version='0.4.4',
    description='Lib to control georide tracker devices with their rest api',
    author='Matthieu DUVAL',
    author_email='georideapilib@duval-dev.fr',
    # use the URL to the github repo
    url='https://github.com/ptimatth/pyGeoride',
    download_url='https://codeload.github.com/ptimatth/pyGeoride/tar.gz/0.1.0',
    keywords=['rest', 'georide', 'api', 'grutier'],  # arbitrary keywords
    classifiers=[],
    install_requires=["python-socketio[client]"],
    tests_require=[
        'pytest>=3.7',
        'pytest-pep8',
        'pytest-cov',
        'python-coveralls',
        'pylint',
        'coverage>=4.4'
    ]
)