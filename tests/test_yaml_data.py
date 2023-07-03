
import pytest
import itertools

from mkdocs.config import load_config
from os import listdir
from os.path import isfile, join

def dict_extract(key, var):
    """Recurse through a dictionary 'var' looking for 'key'."""
    if hasattr(var,'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in dict_extract(key, d):
                        yield result

def peek(iterable):
    """Look into an iterable, like a generator, to extract the first item."""
    try:
        first = next(iterable)
    except StopIteration:
        return None
    return first, itertools.chain([first], iterable)


# Here we're building a list of all the .yaml files in the ./data dir.
# We load all the YAML and test that they have all the keys and values we expect.
config = load_config()
macros = config['plugins']['macros']
services_yaml = macros.config['include_yaml']

@pytest.mark.parametrize("filepath", services_yaml)
def test_service_yaml_data(yaml_data_from_filepath):
    """Validate that YAML data defining the service has all required keys."""

    assert dict_extract('name', yaml_data_from_filepath) is not None
