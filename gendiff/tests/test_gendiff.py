from gendiff.scripts.cli import start
import json
import argparse

parser = argparse.ArgumentParser(description='Compares two configuration'
                                 ' files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', type=str, help='set format of output')
args = parser.parse_args()


def test_gendiff(path1, path2, file): # noqa
    with open(file, 'r') as r:
        text = json.load(r)
        # print(text)
    assert text == start()


if __name__ == '__main__':
    test_gendiff(args.first_file, args.second_file, file="gendiff/tests/fixtures/test_gendiff.json") # noqa
