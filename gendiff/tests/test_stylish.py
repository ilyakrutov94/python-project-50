from gendiff import generate_diff
from gendiff.tests.fixtures.compare_results.stylish_results \
    import file1_file2_json, \
    file3_file4_json, file1_file2_yaml, file3_file4_yaml, \
    filepath1_filepath2_json, file3_1_file3_json, file3_file3_1_json, \
    file5_file6_json, filepath1_filepath2_yaml


def test_gendiff_json():
    input_data1 = ("gendiff/tests/fixtures/json_yaml/file1.json",
                   "gendiff/tests/fixtures/json_yaml/file2.json")
    expected1 = file1_file2_json

    assert generate_diff(*input_data1) == expected1

    input_data2 = ("gendiff/tests/fixtures/json_yaml/file3.json",
                   "gendiff/tests/fixtures/json_yaml/file4.json")
    expected2 = file3_file4_json

    assert generate_diff(*input_data2) == expected2

    input_data3 = ("gendiff/tests/fixtures/json_yaml/file5.json",
                   "gendiff/tests/fixtures/json_yaml/file6.json")
    expected3 = file5_file6_json

    assert generate_diff(*input_data3) == expected3


# def test_gendiff_yaml():
    # input_data1 = ("gendiff/tests/fixtures/json_yaml/file1.yaml",
    #                "gendiff/tests/fixtures/json_yaml/file2.yaml")
    # expected1 = file1_file2_yaml

    # assert generate_diff(*input_data1) == expected1

    # input_data2 = ("gendiff/tests/fixtures/json_yaml/file3.yaml",
    #                "gendiff/tests/fixtures/json_yaml/file4.yaml")
    # expected2 = file3_file4_yaml

    # assert generate_diff(*input_data2) == expected2


def test_gendiff_wrong_file_name():
    input_data1 = "some_file.json", "test/fixtures/json_yaml/file2.json"
    input_data2 = "gendiff/tests/fixtures/json_yaml/file2.json", "some_file.json" # noqa

    try:
        generate_diff(*input_data1)
        assert False
    except FileNotFoundError:
        assert True

    try:
        generate_diff(*input_data2)
        assert False
    except FileNotFoundError:
        assert True


def test_gendiff_json_empty():
    input_data1 = ("gendiff/tests/fixtures/json_yaml/file3.json",
                   "gendiff/tests/fixtures/json_yaml/file3_1.json")
    expected1 = file3_file3_1_json

    assert generate_diff(*input_data1) == expected1

    input_data2 = ("gendiff/tests/fixtures/json_yaml/file3_1.json",
                   "gendiff/tests/fixtures/json_yaml/file3.json")
    expected2 = file3_1_file3_json

    assert generate_diff(*input_data2) == expected2


def test_gendiff_path():
    input_data1 = ("gendiff/tests/fixtures/json_yaml/filepath1.json",
                   "gendiff/tests/fixtures/json_yaml/filepath2.json")
    expected1 = filepath1_filepath2_json

    assert generate_diff(*input_data1) == expected1

    input_data2 = ("gendiff/tests/fixtures/json_yaml/filepath1.yaml",
                   "gendiff/tests/fixtures/json_yaml/filepath2.yaml")
    expected2 = filepath1_filepath2_yaml

    assert generate_diff(*input_data2) == expected2
