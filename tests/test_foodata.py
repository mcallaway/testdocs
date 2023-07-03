
import pytest
import itertools

from utils import dict_extract
from utils import peek

included_yaml = ['data/foodata.yml']

@pytest.mark.parametrize("filepath", included_yaml)
def test_included_yaml_data(yaml_data_from_filepath):
    """Validate that included YAML data has all required keys."""

    assert dict_extract('name', yaml_data_from_filepath) is not None
