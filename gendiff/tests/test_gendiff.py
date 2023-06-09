from gendiff.scripts.gendiff import generate_diff_stylish,\
    generate_diff_plain, generate_diff_raw, generate_diff_json


def test_raw(file="gendiff/tests/fixtures/file3.json"):
    raw = generate_diff_raw("gendiff/tests/fixtures/file1.json",
                            "gendiff/tests/fixtures/file2.json")
    return raw
