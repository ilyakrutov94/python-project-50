from gendiff.scripts.gendiff import generate_diff_stylish
import argparse


def start():
    parser = argparse.ArgumentParser(description='Compares two configuration'
                                     ' files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', type=str, help='set format of output') # noqa
    args = parser.parse_args()
    return generate_diff_stylish(args.first_file, args.second_file)
