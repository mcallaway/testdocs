
import os
import yaml
import pytest
from py.xml import html

@pytest.fixture
def yaml_data_from_header(filepath):
    """Load data from YAML header of a markdown document."""

    basedir = os.path.dirname( os.path.realpath(__file__) )
    realpath = os.path.join(basedir, "..", filepath)

    def get_yaml(f):
        pointer = f.tell()
        if f.readline() != '---\n':
          f.seek(pointer)
          return ''
        readline = iter(f.readline, '')
        readline = iter(readline.__next__, '---\n')
        return ''.join(readline)

    with open(realpath, encoding='UTF-8') as f:
        data = list(yaml.load_all(get_yaml(f), Loader=yaml.SafeLoader))
        return(data)

@pytest.fixture
def yaml_data_from_filepath(filepath):
    """Load data from a YAML document at filepath."""
    basedir = os.path.dirname( os.path.realpath(__file__) )
    realpath = os.path.join(basedir, "..", filepath)
    with open(realpath, "r", encoding='UTF-8') as yamlfile:
        data = yaml.safe_load(yamlfile)
        return(data)

def pytest_html_report_title(report):
    report.title = "DSA Docs Test Results"

def pytest_html_results_table_header(cells):
    del cells[1:]
    cells.append(html.th("File"))
    cells.append(html.th("Name"))
    cells.append(html.th("Parameters"))
    cells.append(html.th("Description"))

def pytest_html_results_table_row(report, cells):
    del cells[1:]
    cells.append(html.td(report.testfile))
    cells.append(html.td(report.testname))
    cells.append(html.td(report.testargs))
    cells.append(html.td(report.description))

def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('Foo output captured.', class_='empty log'))

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    nodeid = report.nodeid
    (testfile,test) = nodeid.split("::")
    (testname, testargs) = test.split("[")
    testargs = testargs.replace("]","")

    report.description = str(item.function.__doc__)
    report.testfile = testfile
    report.testname = testname
    report.testargs = testargs
