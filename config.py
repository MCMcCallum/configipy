"""
Created 05-06-18 by Matthew C. McCallum
"""


# Local imports
# None.

# Third party module imports
import yaml

# Python standard library imports
import os
import json
import hashlib


class Config(dict):
    """
    A simple class that encapsulates feature configuration files stored in yaml format.
    Each feature configuration file should contain all the details that make a feature unique for a certain type, e.g.,
    a CQT.
    """

    # TODO [matt.c.mccallum 07.03.19]: Allow loading a whole folder of configs
    # TODO [matt.c.mccallum 07.03.19]: Allow linking or references between configs to avoid duplication

    def __init__(self, config_file):
        """
        Constructor.

        Args:
            config_file: str, dict or file - A file like object or filename describing a yaml file to load
            this class's configuration from. Alternatively, it can be a dictionary describing the 
        """
        if type(config_file) is str:
            with open(config_file) as f:
                self.update(yaml.safe_load(f))
        elif type(config_file) is dict:
            self.update(config_file)
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
            
    @property
    def json(self):
        """
        Returns a string containing a json version of the dictionary that is unique for a unique configuration,
        and identical for identical configurations.

        Return:
            str - A json formatted string describing the dictionary contents
        """
        return json.dumps(self, sort_keys=True)

    @property
    def hashid(self):
        """
        Returns an identifier that will be the same for identical dictionary contents.
        Note there may be a hash collision here for two distinct contents, but it is very unlikely.

        Return:
            str - A string containing a hex representation of the hashed dictionary.
        """
        return hashlib.sha256(self.json.encode()).hexdigest()
