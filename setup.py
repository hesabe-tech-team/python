from setuptools import setup, find_packages
import codecs
import os
VERSION = '0.0.6'
DESCRIPTION = 'checkout package'
LONG_DESCRIPTION = 'checkout package'
# Setting up
setup(
name="hesabe-checkout-Plugin",
version=VERSION,
author="JS",
author_email="itsupport@hesabe.com",
description=DESCRIPTION,
long_description_content_type="text/markdown",
long_description=LONG_DESCRIPTION,
packages=find_packages(),
install_requires=['requests', 'pycryptodome'],
keywords=['python', 'django', 'hesabe'],
classifiers=[
"Development Status :: 1 - Planning",
"Intended Audience :: Developers",
"Programming Language :: Python :: 3",
"Operating System :: Unix",
"Operating System :: MacOS :: MacOS X",
"Operating System :: Microsoft :: Windows",
]
)