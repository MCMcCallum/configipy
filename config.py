"""
Created 05-06-18 by Matthew C. McCallum
"""


# Local imports
# None.

# Third party module imports
import yaml

# Python standard library imports
import os


class Config(dict):
    """
    A simple class that encapsulates feature configuration files stored in yaml format.
    Each feature configuration file should contain all the details that make a feature unique for a certain type, e.g.,
    a CQT.
    """

    def __init__(self, config_file):
        """
        Constructor.

        Args:
            config_file: str or file - A file like object or filename describing a yaml file to load
            this class's configuration from. 
        """
        if type(config_file) is str:
            with open(config_file) as f:
                self.update(yaml.safe_load(f))
        else:
            self.update(yaml.safe_load(f))

    def Save(self, config_file):
        """
        Saves a the configuration fields in yaml format to disk.

        Args:
            config_file: str or file - A file like object or filename describing a yaml file to save
            this class's configuration to.
        """
        if type(config_file) is str:
            with open(config_file, 'w') as f:
                f.write(yaml.safe_dump({k: v for k, v in self.items()}, default_flow_style=False))
        else:
            config_file.write(yaml.safe_dump({k: v for k, v in self.items()}, default_flow_style=False))
            