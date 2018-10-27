.PHONY: clean test dist dist-upload

clean:
	find . -name '*.py[co]' -delete

test:
	python -m pytest \
		-v \
		--cov=finchan_exts \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

dist-upload:
	twine upload dist/*
