from gendiff.scripts.start import start
import argparse

parser = argparse.ArgumentParser(description='Compares two configuration'
                                 ' files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', type=str, help='set format of output')
args = parser.parse_args()


def test_gendiff(path1, path2):
    some_string = ("- follow: False\n"
                   "  host: hexlet.io\n"
                   "- proxy: 123.234.53.22\n"
                   "- timeout: 50\n"
                   "+ timeout: 20\n"
                   "+ verbose: True")
    assert some_string == start()


if __name__ == '__main__':
    test_gendiff(args.first_file, args.second_file)
