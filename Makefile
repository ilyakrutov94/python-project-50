setup: build publish package-f_install
gendiff:
	poetry run gendiff
start:
	poetry run start
start1:
	poetry run start gendiff/tests/fixtures/file1.json gendiff/tests/fixtures/file2.json
start2:
	poetry run start gendiff/tests/fixtures/file1.yml gendiff/tests/fixtures/file2.yml
start3:
	poetry run start gendiff/tests/fixtures/file3.json gendiff/tests/fixtures/file4.json
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