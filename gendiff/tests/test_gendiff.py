from gendiff.scripts.gendiff import generate_diff
import argparse

parser = argparse.ArgumentParser(description='Compares two configuration'
                                 ' files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', type=str, help='set format of output')
args = parser.parse_args()


def test_gendiff(path1, path2):
    assert ('''- follow: False
          host: hexlet.io
        - proxy: 123.234.53.22
        - timeout: 50
        + timeout: 20
        + verbose: True''') == generate_diff(path1, path2)


if __name__ == '__main__':
    test_gendiff(args.first_file, args.second_file)
