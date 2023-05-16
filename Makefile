setup: build publish package-f_install
gendiff:
	poetry run gendiff
install:
	poetry install
publish:
	poetry publish --dry-run
build:
	poetry build
package-install:
	python3 -m pip install --user dist/*.whl
package-f_install:
	pip install --user dist/*.whl --force-reinstall