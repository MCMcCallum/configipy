"""
Created 06-29-18 by Matt C. McCallum
"""


# Local imports
from .configurable import Configurable

# Third party imports
# None.

# Python standard library imports
import sys
import inspect


def class_for_config(module, config, base_class=Configurable):
    """
    Returns a class for a given configuration. 
    It is expected that the class configuration in the config dict is under the key of 
    the class name at the root level of the config dictionary.
    If there are multiple classes matching in the configuration dictionary, they can either
    be separated out before calling this function, or the user can specify a base class, of
    which the returned class must be a child of. Thereby essentially filtering the potential
    classes by the base class.

    Args:
        module -> module - The module in which to search for classes in.

        config -> dict - The configuration dictionary to find a matching class for. Note that
        the root keys in this dictionary must match one and only one class that is a child of
        "base_class".

        base_class -> class - The base class, of which the returned class must be a 
        child of.

    Return:
        dict -> The set of configuration parameters for config that were under the key of the
        matching class

        class -> The class whose name matches a root key in the config dict.
    """
    # Get module details
    parent_module_name = module.__name__
    feature_classes = inspect.getmembers(sys.modules[parent_module_name], inspect.isclass)    # => Note returns a 2 element tuple, the first element is the class name as a string and the second element the class itself.
    feature_classes = [f_class[1] for f_class in feature_classes if issubclass(f_class[1], base_class)]
    feature_class_names = [f_class.__name__ for f_class in feature_classes]

    # Search for matching configuration
    config_fields = config.keys()
    matching_classes = [c_field for c_field in config_fields if c_field in feature_class_names]
    if not len(matching_classes):
        raise KeyError('Provided configuration does not match any, or matches multiple classes in the provided module')

    # Get all matching classes
    f_classes = [feature_classes[feature_class_names.index(match_cls)] for match_cls in matching_classes]

    # Return one class if there is only one
    if len(f_classes) == 1:
        return f_classes[0]

    # Otherwise return the list of classes
    return f_classes
