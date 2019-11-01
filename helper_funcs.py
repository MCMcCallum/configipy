"""
Created 10-16-19 by Matt C. McCallum
"""


# Local imports
from . import features

# Third party imports
# None.

# Python standard library imports
# None.


def _all_subclasses(cls):
    """
    cls.__subclasses__ only transcends one level of inheretance so this is a simple 
    recursion to find all subclasses.

    Args:
        cls: object - The class to find all subclasses for.
    """
    return list(set(cls.__subclasses__()).union([s for c in cls.__subclasses__() for s in _all_subclasses(c)]))


def class_for_config(base_class, config):
    """
    Returns the feature class for a given config dictionary or Configipy Config object.
    This class search is performed under the assumption that each key in the dictionary
    or Config is a class in the pandafeet features module.

    Args:
        base_class: object - 

        config: dict - A dictionary with the keys specifying class names in the pandafeet
        features module.
    """
    fclsses = _all_subclasses(features.timeline_feature.TimelineFeature)
    feature_class_names = [clsobj.__name__ for clsobj in fclsses]

    # Search for matching configuration
    config_fields = config.keys()
    matching_classes = [c_field for c_field in config_fields if c_field in feature_class_names]
    if not len(matching_classes):
        print(feature_class_names)
        print(config_fields)
        raise KeyError('Provided configuration does not match any, or matches multiple classes in the provided module')

    # Get all matching classes
    f_classes = [fclsses[feature_class_names.index(match_cls)] for match_cls in matching_classes]

    # Return one class if there is only one
    if len(f_classes) == 1:
        return f_classes[0]

    # Otherwise return the list of classes
    return f_classes
