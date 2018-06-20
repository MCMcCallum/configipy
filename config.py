"""
Created 05-06-18 by Matthew C. McCallum
"""


# Local imports
from data_access import dir_funcs

# Third party module imports
import yaml

# Python standard library imports
import os


CONFIG_PATHS = [os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config/')]


def add_config_path(path):
    """
    Sets the path to the yaml configuration files that is searched for these files.

    Args:
        path -> str - A string describing an absolute path to a set of configuration files.
    """
    global CONFIG_PATHS
    CONFIG_PATHS += [path]
    config_files = dir_funcs.get_filenames(path, ['.yaml'])
    num_files = len([fname for fname in config_files if fname.rfind('_v')>=0])
    print("Found " + str(num_files) + " configuration files.")


class Config(dict):
    """
    A simple class that encapsulates feature configuration files stored in yaml format.
    Each feature configuration file should contain all the details that make a feature unique for a certain type, e.g.,
    a CQT.

    # TODO [matthew.mccallum 06.16.18]: This config module should be moved to the parent repo, or perhaps a separate module, it isn't really specific to data creation. It could be used for just regular analysis too.
    """

    def __init__(self, version_str='v0.0'):
        """
        Constructor.

        Args:
             version_str -> str - A string specifying which feature configuration to get.
        """
        config_files = []
        for cfg_path in CONFIG_PATHS:
            config_files += dir_funcs.get_filenames(CONFIG_PATH, ['.yaml'])
        config_names = [os.path.splitext(os.path.basename(name))[0] for name in config_files]
        config_names = [name[(name.rfind('_v')+1):] for name in config_names]
        config_file = config_files[config_names.index(version_str)]
        with open(config_file) as f:
            self.update(yaml.safe_load(f))
