
.PHONY: build test report serve open clean distclean deploy

build:
	mkdocs build

serve:
	mkdocs serve

# This assumes GitHub repo Settings have Pages configured,
# and set to the 'gh-deploy' branch and the '/' directory.
deploy:
	mkdocs gh-deploy

test:
	pytest -sv

report:
	pytest --html-report=./docs/report/ --self-contained-html --title="PyTest Report"

open:
	open http://127.0.0.1:8000

distclean:
	rm -f report/*
	rm -rf site/*

