"""
Created 03-06-19 by Matt C. McCallum
"""


# Local imports
# None.

# Third party imports
# None.

# Python standard library imports
import setuptools


REQUIRED_PACKAGES = [
    'pyyaml'
]


setuptools.setup(
    name='configipy',
    version='0.0.1',
    description='A python module for configuring hierarchical class structures in yaml with defaults',
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages()
)
