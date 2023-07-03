
import pytest
import itertools

from mkdocs.config import load_config
from os import listdir
from os.path import isfile, join

from utils import dict_extract
from utils import peek

# Here we're building a list of all the .yaml files in the ./data dir.
# We load all the YAML and test that they have all the keys and values we expect.
config = load_config()
macros = config['plugins']['macros']
included_yaml = macros.config['include_yaml']

@pytest.mark.parametrize("filepath", included_yaml)
def test_included_yaml_data(yaml_data_from_filepath):
    """Validate that included YAML data has all required keys."""

    assert dict_extract('name', yaml_data_from_filepath) is not None
