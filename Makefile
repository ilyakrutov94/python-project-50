setup: build publish package-f_install
gendiff:
	poetry run cli
start:
	poetry run cli
start1:
	poetry run cli gendiff/tests/fixtures/file1.json gendiff/tests/fixtures/file2.json
start2:
	poetry run cli gendiff/tests/fixtures/file1.yml gendiff/tests/fixtures/file2.yml
start3:
	poetry run cli gendiff/tests/fixtures/file3.json gendiff/tests/fixtures/file4.json
install:
	poetry install
publish:
	poetry publish --dry-run
build:
	poetry build
package-user_install:
	python3 -m pip install --user dist/*.whl
package-install:
	python3 -m pip install dist/*.whl
package-f_user_install:
	pip install --user dist/*.whl --force-reinstall
package-f_install:
	pip install dist/*.whl --force-reinstall