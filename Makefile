
.PHONY: build serve open clean distclean

build:
	mkdocs build

serve:
	mkdocs serve

report: report/pytest_html_report.html
report/pytest_html_report.html:
	pytest --html-report=./report/ --self-contained-html --title="PyTest Report"

distclean:
	rm -f report/*

clean: distclean

open: report
	open report/pytest_html_report.html
