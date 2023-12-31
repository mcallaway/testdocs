
import pytest

from lib.foo import Foo

included_yaml = ['data/foodata.yml']

@pytest.mark.parametrize("filepath", included_yaml)
def test_included_yaml_data(yaml_data_from_filepath):
    """Validate that included YAML data has all required keys."""

    assert Foo(yaml_data_from_filepath['foodata'])