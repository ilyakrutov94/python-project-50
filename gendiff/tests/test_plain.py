from gendiff.formatters.plain import make_plain, _get_value
from gendiff import generate_diff
from gendiff.tests.fixtures.compare_results.plain_results \
    import file1_file2_json, \
    file3_file4_json, file1_file2_yaml, file3_file4_yaml, \
    filepath1_filepath2_json, file3_1_file3_json, file3_file3_1_json, \
    file5_file6_json


def test_gendiff_path():
    input_data1 = ("gendiff/tests/fixtures/json_yaml/filepath1.json",
                   "gendiff/tests/fixtures/json_yaml/filepath2.json")
    expected = filepath1_filepath2_json

    assert generate_diff(*input_data1, "plain") == expected


def test_gendiff_yaml():
    input_data1 = ("gendiff/tests/fixtures/json_yaml/file1.yaml",
                   "gendiff/tests/fixtures/json_yaml/file2.yaml")

    expected1 = file1_file2_yaml

    assert generate_diff(*input_data1, "plain") == expected1

    input_data2 = ("gendiff/tests/fixtures/json_yaml/file3.yaml",
                   "gendiff/tests/fixtures/json_yaml/file4.yaml")
    expected2 = file3_file4_yaml

    assert generate_diff(*input_data2, "plain") == expected2
