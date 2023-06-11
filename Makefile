setup: build publish install
publish:
	poetry publish --dry-run
build:
	poetry build
lint:
	poetry run flake8 gendiff/
install:
	pip install dist/*.whl --force-reinstall
test:
	poetry run pytest
main1:
	poetry run python3 gendiff/scripts/main.py gendiff/tests/fixtures/json_yaml/filepath1.json gendiff/tests/fixtures/json_yaml/filepath2.json -f plain
main2:
	poetry run python3 gendiff/scripts/main.py gendiff/tests/fixtures/json_yaml/filepath1.json gendiff/tests/fixtures/json_yaml/filepath2.json -f stylish
main3:
	poetry run python3 gendiff/scripts/main.py gendiff/tests/fixtures/json_yaml/filepath1.json gendiff/tests/fixtures/json_yaml/filepath2.json -f json
test-coverage:
	poetry run pytest --cov-report term-missing --cov=gendiff --cov-report xml