
import pytest

from lib.bar import Bar

included_yaml = ['data/bardata.yml']

@pytest.mark.parametrize("filepath", included_yaml)
def test_included_yaml_data(yaml_data_from_filepath):
    """Validate that included YAML data has all required keys."""

    assert Bar(yaml_data_from_filepath['bardata'])