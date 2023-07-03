
.PHONY: build serve open clean distclean

build:
	mkdocs build

serve:
	mkdocs serve

report: report.html
report.html:
	pytest --html-report=./report.html --self-contained-html
#	pytest --html=report.html --self-contained-html

distclean:
	rm report.html

clean: distclean

open: report.html
	open report.html
