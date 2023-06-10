setup: build publish install
test-cov:
	poetry run pytest --cov=gendiff --cov-report xml
publish:
	poetry publish --dry-run
build:
	poetry build
lint:
	poetry run flake8 gendiff/
install:
	pip install dist/*.whl --force-reinstall
test:
	poetry run pytest -vv
main1:
	poetry run python3 gendiff/scripts/main.py gendiff/tests/fixtures/json_yaml/file3.json gendiff/tests/fixtures/json_yaml/file4.json -f plain
main2:
	poetry run python3 gendiff/scripts/main.py gendiff/tests/fixtures/json_yaml/file3.json gendiff/tests/fixtures/json_yaml/file4.json -f stylish
main3:
	poetry run python3 gendiff/scripts/main.py gendiff/tests/fixtures/json_yaml/file3.json gendiff/tests/fixtures/json_yaml/file4.json -f json