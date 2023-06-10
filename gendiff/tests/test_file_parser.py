from gendiff.file_parser import open_file, parse_file


def test_open_file_non_empty_file():
    path = 'gendiff/tests/fixtures/json_yaml/file1.json'
    expected = """{
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": false
}"""
    assert open_file(path) == expected


def test_open_file_empty_file():
    path = 'gendiff/tests/fixtures/json_yaml/empty.json'
    expected = ''
    assert open_file(path) == expected


def test_open_file_non_existing_file():
    path = "non_exist.json"
    try:
        open_file(path)
        assert False
    except FileNotFoundError:
        assert True


def test_load_json_yaml():
    path_json = 'gendiff/tests/fixtures/json_yaml/file1.json'
    expected_json = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    assert parse_file(path_json) == expected_json

    path_yaml = 'gendiff/tests/fixtures/json_yaml/file_for_test.yaml'
    expected_yaml = {
        "Bakery": [
            "Sourdough loaf",
            "Bagels"
        ],
        "Cheesemonger": [
            "Blue cheese",
            "Feta"
        ]
    }
    assert parse_file(path_yaml) == expected_yaml
