
.PHONY: build serve open clean distclean deploy

build:
	mkdocs build

serve:
	mkdocs serve

# This assumes GitHub repo Settings have Pages configured,
# and set to the 'gh-deploy' branch and the '/' directory.
deploy:
	mkdocs gh-deploy

report: report/pytest_html_report.html
report/pytest_html_report.html:
	pytest --html-report=./report/ --self-contained-html --title="PyTest Report"

distclean:
	rm -f report/*

clean: distclean

open: report
	open report/pytest_html_report.html
